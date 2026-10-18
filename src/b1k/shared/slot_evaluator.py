"""Persistent-simulator evaluation: the official BatchedEvaluator, refilled one env slot at a time.

Upstream evaluates one fixed batch per process (a new batch needs a new simulator boot, and every env waits
for the slowest episode). SlotEvaluator keeps the simulator alive and loads the next instance into a slot as
soon as its episode ends, while the other slots keep running. Every scene is saved at boot and restored
before each later instance, so each episode starts like the first episode of a freshly booted simulator
(upstream otherwise keeps whatever the previous episode did outside the task scope).
"""

import copy
import json
import os
import pathlib
import random
import time

import numpy as np
import torch as th

import omnigibson as og
from omnigibson.eval import evaluator as evaluator_module
from omnigibson.eval.evaluator import BatchedEvaluator
from omnigibson.eval.utils.network_utils import WebsocketClientPolicy

from b1k.shared.eval_b1k_wrapper import ACTIVE_ENVS_KEY

AFFINITY_ENV = "B1K_EVAL_CPU_AFFINITY"


class SlotWebsocketPolicy:
    """omnigibson.eval.policies.WebsocketPolicy plus `reset_envs`: resets only some environments' state
    on serve_b1k.py."""

    def __init__(self, *args, host: str = "127.0.0.1", port: int = 8000, **kwargs) -> None:
        self.policy = WebsocketClientPolicy(host=host, port=port)

    def forward(self, obs: dict, *args, **kwargs) -> th.Tensor:
        return self.policy.act(obs).detach().cpu()

    def reset(self) -> None:
        self.policy.reset()

    def reset_envs(self, env_indices: list[int]) -> None:
        client = self.policy
        if client._ws is None:
            client._ws, client._server_metadata = client._wait_for_server()
        client._ws.send(client._packer.pack({"reset": True, "env_indices": [int(i) for i in env_indices]}))


def clear_episode_grasps(robot) -> None:
    """Release this robot's assisted grasps before a new instance teleports it (the held object would move)."""
    if not robot.is_manipulation or robot.grasping_mode == "physical":
        return
    for arm in robot.arm_names:
        robot.release_grasp_immediately(arm=arm)
        robot._ag_obj_in_hand[arm] = None
        robot._ag_obj_constraint_params[arm] = None
        robot._ag_release_counter[arm] = None
        robot._ag_grasp_counter[arm] = None


class SlotEvaluator(BatchedEvaluator):
    def __init__(self, cfg, *, output_dir: pathlib.Path, write_video: bool = False, video_fps: int = 30) -> None:
        super().__init__(cfg)
        self._boot_scenes = [scene.save(as_dict=True) for scene in self.env.scenes]
        self._boot_rng = _rng_state()
        self._scene_used = [False] * self.num_envs
        self._pinned = False
        self.output_dir = pathlib.Path(output_dir)
        (self.output_dir / "json").mkdir(parents=True, exist_ok=True)
        if write_video:
            (self.output_dir / "videos").mkdir(parents=True, exist_ok=True)
        self.write_video = write_video
        self.video_fps = video_fps
        self.episodes = [None] * self.num_envs  # per slot: (instance_id, rollout_id, steps)

    @property
    def active_slots(self) -> list[int]:
        return [slot for slot, episode in enumerate(self.episodes) if episode is not None]

    @property
    def free_slots(self) -> list[int]:
        return [slot for slot, episode in enumerate(self.episodes) if episode is None]

    def _load_instance_state(self, instance_id: int, instance_eval_state) -> None:
        accessor = instance_eval_state.env_accessor
        clear_episode_grasps(accessor.robot)
        if self._scene_used[accessor.env_idx]:
            # restore() keeps references into the file it is given
            self.env.scenes[accessor.env_idx].restore(copy.deepcopy(self._boot_scenes[accessor.env_idx]))
            _set_rng_state(self._boot_rng)
        self._scene_used[accessor.env_idx] = True
        super()._load_instance_state(instance_id, instance_eval_state)

    def load_slots(self, assignments: dict[int, tuple[int, int]]) -> None:
        """Load {slot: (instance_id, rollout_id)}; the other running slots continue where they were."""
        loaded = sorted(assignments)
        others = self.active_slots
        saved = {slot: self.env.scenes[slot].dump_state(serialized=False) for slot in others}
        for slot in loaded:
            state = self.instance_eval_states[slot]
            state.instance_id, state.active = int(assignments[slot][0]), True
            self._load_instance_state(state.instance_id, state)
        self._settle_and_finalize(loaded)
        env_indices = th.tensor(loaded, dtype=th.long)
        obs_list, _ = self.env.reset(env_indices=env_indices)
        for slot in others:
            self.env.scenes[slot].load_state(saved[slot], serialized=False)
        for slot in loaded:
            self._reset_light_synchronizer(self.instance_eval_states[slot])
        if self.should_sync_lights:
            for _ in range(3):
                og.sim.render()
            obs_list, _ = self.env.get_obs(env_indices=env_indices)
        self.policy.reset_envs(loaded)
        for i, slot in enumerate(loaded):
            state = self.instance_eval_states[slot]
            state.obs = self._preprocess_obs(obs_list[i], state)
            for metric in state.metrics:
                metric.reset()
            instance_id, rollout_id = assignments[slot]
            self.episodes[slot] = [int(instance_id), int(rollout_id), 0]
            if self.write_video:
                path = self.output_dir / "videos" / f"{self.cfg.task.name}_{instance_id}_{rollout_id}.mp4"
                self._set_video_writer(
                    state, evaluator_module.create_video_writer(fpath=str(path), resolution=(448, 672), rate=self.video_fps)
                )

    def step(self) -> list[dict]:
        """Step every slot once; returns the results of the episodes that ended."""
        if not self._pinned:
            # pin here, not at start: the simulator spawns most of its threads while booting
            self._pinned = True
            if os.environ.get(AFFINITY_ENV):
                os.sched_setaffinity(0, {int(c) for c in os.environ[AFFINITY_ENV].split(",")})
        active = self.active_slots
        template = next(s.obs for s in self.instance_eval_states if s.obs is not None)
        request = {
            key: th.stack([s.obs[key] if s.obs is not None else th.zeros_like(template[key]) for s in self.instance_eval_states])
            for key in template
        }
        request[ACTIVE_ENVS_KEY] = th.tensor([e is not None for e in self.episodes])
        batched_action = self.policy.forward(obs=request)
        if batched_action.ndim == 1:
            batched_action = batched_action.unsqueeze(0)
        actions = th.zeros((self.num_envs, self.instance_eval_states[0].env_accessor.robot.action_dim))
        for slot in active:
            actions[slot] = batched_action[slot].to(actions.dtype)
        terminated, truncated, _ = self._apply_actions(actions, active)
        results = []
        for slot in active:
            self.episodes[slot][2] += 1
            if self.write_video:
                self._write_video(self.instance_eval_states[slot])
            if terminated[slot] or truncated[slot]:
                results.append(self._finish(slot))
        return results

    def _finish(self, slot: int) -> dict:
        instance_id, rollout_id, steps = self.episodes[slot]
        state = self.instance_eval_states[slot]
        state.active = False
        self.n_trials += 1
        self.n_success_trials += int(state.env_accessor.success)
        result = {"task": self.cfg.task.name, "instance_id": instance_id, "rollout_id": rollout_id, "steps": steps,
                  "success": state.env_accessor.success, "env_slot": slot, "finished_at": time.time()}
        for metric in state.metrics:
            result.update(metric.aggregate())
        with open(self.output_dir / "json" / f"{self.cfg.task.name}_{instance_id}_{rollout_id}.json", "w") as f:
            json.dump(result, f, indent=2, default=float)
        if self.write_video:
            self._set_video_writer(state, None)
        self.episodes[slot] = None
        return result


def _rng_state() -> tuple:
    cuda = th.cuda.get_rng_state_all() if th.cuda.is_available() else None
    return random.getstate(), np.random.get_state(), th.get_rng_state(), cuda


def _set_rng_state(state: tuple) -> None:
    python, numpy_state, torch_cpu, cuda = state
    random.setstate(python)
    np.random.set_state(numpy_state)
    th.set_rng_state(torch_cpu)
    if cuda is not None:
        th.cuda.set_rng_state_all(cuda)
