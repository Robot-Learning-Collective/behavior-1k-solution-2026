"""B1K policy wrapper with action compression, rolling inpainting, boundary snap, and stage voting."""

import dataclasses
import json
import logging
import math
import pathlib
from collections import deque

import numpy as np
import torch

from openpi_client.base_policy import BasePolicy
from openpi_client.image_tools import resize_with_pad
from b1k.policies.b1k_policy import extract_state_from_proprio
from b1k.models.pi_behavior_config import TASK_NUM_STAGES
from b1k.shared.correction_rules import gripper_open_correction

logger = logging.getLogger(__name__)

RESIZE_SIZE = 224
STAGE_LEN_STATS = pathlib.Path(__file__).resolve().parents[3] / "assets" / "semantic_stages" / "stage_len_stats.json"
# (num_envs,) bool in batched requests: env slots without a running episode get no inference and a zero action
ACTIVE_ENVS_KEY = "b1k_active_envs"


@dataclasses.dataclass
class B1KWrapperConfig:
    """Configuration for B1K policy wrapper execution parameters."""
    # Execute the first 26 predicted actions in 13 env steps (cubic resampling, base velocities scaled 2x)
    # and keep the next 4 as the soft inpainting anchor of the next prediction
    actions_to_execute: int = 26
    actions_to_keep: int = 4
    execute_in_n_steps: int = 13
    # Stage voting over the predictions of the last `stage_vote_window_steps` env steps: promote when
    # votes_to_promote / history_len of them predict the next stage
    history_len: int = 3
    votes_to_promote: int = 2
    stage_vote_window_steps: int = 120
    # A stage is left only after min_stage_frac x the shortest demo duration of that stage
    min_stage_frac: float = 0.67
    # Shift each new chunk to continue from the last executed action; the shift decays by this per step
    boundary_snap_decay: float = 0.7
    apply_eval_tricks: bool = True


class B1KPolicyWrapper():
    """B1K policy wrapper for PI_BEHAVIOR models with action compression, rolling inpainting, and stage voting."""

    def __init__(
        self,
        policy: BasePolicy,
        text_prompt: str = "PI_BEHAVIOR model (task-conditioned)",  # Not used, kept for compatibility
        action_horizon: int = 30,
        task_id: int | None = None,
        config: B1KWrapperConfig = None,
    ) -> None:
        self.policy = policy
        self.text_prompt = text_prompt
        self.action_horizon = action_horizon
        self.config = config if config is not None else B1KWrapperConfig()

        # Validate configuration
        if self.config.actions_to_execute + self.config.actions_to_keep > self.action_horizon:
            raise ValueError(
                f"actions_to_execute + actions_to_keep exceeds action_horizon"
            )
        self.stage_len_stats = json.loads(STAGE_LEN_STATS.read_text())["stats"]

        # PI_BEHAVIOR specific (always True for B1K)
        self.task_id = task_id
        self.current_stage = 0
        self.stage_entered_step = 0
        self.prediction_history = deque()  # (env step, predicted stage)

        # Control loop variables
        self.last_actions = None
        self.action_index = 0
        self.step_count = 0
        self.prediction_count = 0
        self.next_initial_actions = None
        self.last_executed_action = None

    def reset(self):
        """Reset policy state."""
        self.policy.reset()
        self.last_actions = None
        self.action_index = 0
        self.step_count = 0
        self.prediction_count = 0
        self.next_initial_actions = None
        self.last_executed_action = None
        self.current_stage = 0
        self.stage_entered_step = 0
        self.prediction_history.clear()
        logger.info(f"Policy reset - Task ID: {self.task_id}, Action horizon: {self.action_horizon}")

    def _handle_task_change(self, new_task_id):
        """Reset rollout state on a task ID change."""
        if self.task_id != new_task_id:
            old_task_id = self.task_id
            self.task_id = new_task_id

            logger.info(f"🔄 Task change detected: {old_task_id} → {new_task_id} (max stages: {TASK_NUM_STAGES[new_task_id]})")

            self.current_stage = 0
            self.stage_entered_step = self.step_count
            self.prediction_history.clear()
            self.last_actions = None
            self.action_index = 0
            self.next_initial_actions = None
            self.last_executed_action = None

    def process_obs(self, obs: dict) -> dict:
        """Process observation to match model input format."""
        prop_state = obs["robot_r1::proprio"]

        head_original = obs["robot_r1::robot_r1:zed_link:Camera:0::rgb"][..., :3]
        left_original = obs["robot_r1::robot_r1:left_realsense_link:Camera:0::rgb"][..., :3]
        right_original = obs["robot_r1::robot_r1:right_realsense_link:Camera:0::rgb"][..., :3]

        # Resize images
        head_resized = resize_with_pad(head_original, RESIZE_SIZE, RESIZE_SIZE)
        left_resized = resize_with_pad(left_original, RESIZE_SIZE, RESIZE_SIZE)
        right_resized = resize_with_pad(right_original, RESIZE_SIZE, RESIZE_SIZE)

        return {
            "observation/egocentric_camera": head_resized,
            "observation/wrist_image_left": left_resized,
            "observation/wrist_image_right": right_resized,
            "observation/state": prop_state,
            "prompt": self.text_prompt,
        }

    def _enter_stage(self, stage: int, reason: str):
        logger.info(f"{reason}: {self.current_stage} → {stage} (task {self.task_id}, step {self.step_count})")
        self.current_stage = stage
        self.stage_entered_step = self.step_count
        self.prediction_history.clear()

    def update_current_stage(self, predicted_subtask_logits):
        """Update current stage by majority voting over a window of env steps (independent of the replanning
        cadence); transitions need the votes to span 2/3 of the window."""
        if self.task_id is None:
            return

        max_stage = TASK_NUM_STAGES[self.task_id] - 1
        predicted_stage = min(int(np.argmax(predicted_subtask_logits)), max_stage)

        self.prediction_history.append((self.step_count, predicted_stage))
        while self.prediction_history[0][0] <= self.step_count - self.config.stage_vote_window_steps:
            self.prediction_history.popleft()
        votes = [stage for _, stage in self.prediction_history]
        span = self.step_count - self.prediction_history[0][0]
        if len(votes) < self.config.history_len or span < (self.config.stage_vote_window_steps * 2) // 3:
            return

        next_stage = self.current_stage + 1
        if next_stage <= max_stage:
            votes_for_next = sum(1 for pred in votes if pred == next_stage)
            votes_to_skip = sum(1 for pred in votes if pred == next_stage + 1)
            votes_to_go_back = sum(1 for pred in votes if pred == self.current_stage - 1)
            # demo stage lengths are in 30 fps frames, executed at execute_in_n_steps / actions_to_execute
            min_frames = self.stage_len_stats[str(self.task_id)][self.current_stage]["min"]
            min_steps = int(self.config.min_stage_frac * min_frames * self.config.execute_in_n_steps / self.config.actions_to_execute)
            may_leave = self.step_count - self.stage_entered_step >= min_steps

            if votes_for_next >= math.ceil(self.config.votes_to_promote / self.config.history_len * len(votes)):
                if may_leave:
                    self._enter_stage(next_stage, "⬆️  Stage advanced")
            elif votes_to_skip == len(votes):
                if may_leave:
                    self._enter_stage(next_stage, "⏭️  Stage skipped")
            elif votes_to_go_back == len(votes) and self.current_stage > 0:
                self._enter_stage(self.current_stage - 1, "⬅️  Stage went back")

    def prepare_batch_for_pi_behavior(self, batch):
        """Prepare batch for PI_BEHAVIOR model by adding task_id and current_stage."""
        task_id = self.task_id if self.task_id is not None else -1
        batch_copy = batch.copy()
        if "prompt" in batch_copy:
            del batch_copy["prompt"]

        batch_copy["tokenized_prompt"] = np.array([task_id, self.current_stage], dtype=np.int32)
        batch_copy["tokenized_prompt_mask"] = np.array([True, True], dtype=bool)
        batch_copy["subtask_state"] = np.array(self.current_stage, dtype=np.int32)

        return batch_copy

    def _interpolate_actions(self, actions, target_steps):
        """Interpolate actions using cubic spline."""
        from scipy.interpolate import interp1d

        original_indices = np.linspace(0, len(actions)-1, len(actions))
        target_indices = np.linspace(0, len(actions)-1, target_steps)

        interpolated = np.zeros((target_steps, actions.shape[1]))
        for dim in range(actions.shape[1]):
            f = interp1d(original_indices, actions[:, dim], kind='cubic')
            interpolated[:, dim] = f(target_indices)

        return interpolated

    def act(self, obs: dict) -> torch.Tensor:
        """Main action function."""
        model_input = self.begin_step(obs)
        if model_input is None:
            return self.end_step(None)
        if model_input.get("initial_actions") is not None:
            return self.end_step(self.policy.infer(model_input, initial_actions=model_input["initial_actions"]))
        return self.end_step(self.policy.infer(model_input))

    def begin_step(self, obs: dict) -> dict | None:
        """The model input if this step starts a new chunk, else None (the caller runs the policy)."""
        # Extract task_id from observations
        if "task_id" in obs:
            self._handle_task_change(int(np.asarray(obs["task_id"]).reshape(-1)[0]))

        self._current_state = extract_state_from_proprio(obs["robot_r1::proprio"])
        if self.last_actions is not None and self.action_index < self.config.execute_in_n_steps:
            return None
        model_input = self.prepare_batch_for_pi_behavior(self.process_obs(obs))
        # Rolling inpainting anchor from the previous chunk
        if self.next_initial_actions is not None:
            model_input["initial_actions"] = self.next_initial_actions
        return model_input

    def end_step(self, output: dict | None) -> torch.Tensor:
        """Consume the policy output (None when begin_step returned None) and return this step's action."""
        if output is not None:
            actions = output["actions"]

            # Ensure correct shape
            if len(actions.shape) == 3:
                actions = actions[0]

            # Open a fully closed gripper in stages where the demos never close it
            if self.config.apply_eval_tricks and self.task_id is not None:
                actions = gripper_open_correction(self.task_id, self.current_stage, self._current_state, actions)

            actions_to_execute = self.config.actions_to_execute
            execute_steps = self.config.execute_in_n_steps

            # Save actions for next inpainting (before compression)
            inpainting_end = actions_to_execute + self.config.actions_to_keep
            self.next_initial_actions = actions[actions_to_execute:inpainting_end].copy()

            # Extract and compress actions
            self.last_actions = self._interpolate_actions(actions[:actions_to_execute], execute_steps)
            self.last_actions[:, :3] *= actions_to_execute / execute_steps  # Scale velocities

            # Boundary snap: start exactly at the last executed action, handing over to the new plan
            if self.config.boundary_snap_decay > 0 and self.last_executed_action is not None:
                decay = self.config.boundary_snap_decay ** np.arange(len(self.last_actions))
                self.last_actions += (self.last_executed_action - self.last_actions[0])[None, :] * decay[:, None]

            self.action_index = 0
            self.prediction_count += 1

            # Log prediction details (at lower frequency, every 10 predictions)
            if self.prediction_count % 10 == 0:
                logger.info(f"🎯 Prediction #{self.prediction_count} | Actions: compressed {actions_to_execute}→{execute_steps} | Inpainting: {self.next_initial_actions is not None}")

            # Update stage based on model predictions
            if "subtask_logits" in output:
                self.update_current_stage(output["subtask_logits"])

        current_action = self.last_actions[self.action_index]
        self.last_executed_action = current_action.copy()
        self.action_index += 1
        self.step_count += 1

        # Log progress every 100 steps
        if self.step_count % 100 == 0:
            logger.info(f"📊 Step {self.step_count} | Task: {self.task_id} | Stage: {self.current_stage}/{TASK_NUM_STAGES[self.task_id]-1} | Predictions: {self.prediction_count}")

        return torch.from_numpy(current_action).float()


def act_batched(policies: list[B1KPolicyWrapper], obs: dict) -> torch.Tensor:
    """One step of N environments: obs values are (N, ...) arrays and policies[i] holds env i's rollout state.
    Environments that start a new chunk share one batched model call, padded to N so JAX compiles once."""
    n = len(policies)
    active = obs.pop(ACTIVE_ENVS_KEY, None)
    active = [True] * n if active is None else [bool(a) for a in np.asarray(active).reshape(-1)]
    per_env = [{k: v[i] if isinstance(v, np.ndarray) else v for k, v in obs.items()} for i in range(n)]
    inputs = [p.begin_step(o) if a else None for p, o, a in zip(policies, per_env, active)]
    idx = [i for i, model_input in enumerate(inputs) if model_input is not None]
    outputs = [None] * n
    if idx:
        batch = [(inputs[i], inputs[i].get("initial_actions")) for i in idx]
        for i, out in zip(idx, policies[0].policy.infer_batch(batch, pad_to=n)):
            outputs[i] = out
    actions = [p.end_step(out) if a else torch.zeros(23) for p, out, a in zip(policies, outputs, active)]
    return torch.stack(actions)
