"""Persistent BEHAVIOR eval worker driven by run_parallel_eval.py over stdin/stdout.

    worker -> "@@WORKER_READY"       a slot is free (one line per free slot)
    parent -> "<instance index>"     evaluate this instance index of --mode
    parent -> "EXIT"                 no more work: finish the running episodes and exit
    worker -> "@@WORKER_OK <idx>"    instance finished (all rollouts)
    worker -> "@@WORKER_FAIL <idx>"  for every instance held when the worker crashes (the parent requeues)
"""

import argparse
import os
import sys
import traceback
from pathlib import Path

from omegaconf import OmegaConf

from omnigibson.eval.evaluator import resolve_instance_ids
from omnigibson.eval.utils.eval_utils import DEFAULT_EVAL_SEED, seed_everything
from omnigibson.macros import gm

from b1k.shared.slot_evaluator import SlotEvaluator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-name", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--mode", choices=("train", "public_test", "hidden_test"), default="public_test")
    parser.add_argument("--num-envs", type=int, default=1, help="Env slots in this simulator")
    parser.add_argument("--num-rollouts", type=int, default=1)
    parser.add_argument("--max-steps", type=int, default=None)
    parser.add_argument("--robot-config", default=None)
    parser.add_argument("--env-wrapper", default="omnigibson.eval.wrappers.DefaultWrapper")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--write-video", action=argparse.BooleanOptionalAction, default=False)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    gm.HEADLESS = True
    gm.RENDER_VIEWER_CAMERA = False  # headless runs read the robot cameras only
    cfg = OmegaConf.create({
        "env_wrapper": {"_target_": args.env_wrapper},
        "policy_name": "websocket",
        "model": {"_target_": "b1k.shared.slot_evaluator.SlotWebsocketPolicy", "host": args.host, "port": args.port},
        "headless": True,
        "partial_scene_load": True,
        "max_steps": args.max_steps,
        "write_video": args.write_video,
        "mode": args.mode,
        "seed": seed_everything(DEFAULT_EVAL_SEED),
        "num_envs": args.num_envs,
        "task": {"name": args.task_name},
        "robot": OmegaConf.load(os.path.expanduser(args.robot_config)) if args.robot_config else None,
    })

    held, rollouts_left, draining = {}, {}, False  # slot -> instance index / remaining rollouts
    with SlotEvaluator(cfg, output_dir=Path(args.output_dir), write_video=args.write_video) as evaluator:
        try:
            while True:
                assignments = {}
                for slot in evaluator.free_slots:
                    if slot not in held:
                        if draining:
                            continue
                        print("@@WORKER_READY", flush=True)
                        line = sys.stdin.readline().strip()
                        if not line or line == "EXIT":
                            draining = True
                            continue
                        held[slot], rollouts_left[slot] = int(line), args.num_rollouts
                    instance_id = resolve_instance_ids(args.task_name, [held[slot]], mode=args.mode)[0]
                    assignments[slot] = (instance_id, args.num_rollouts - rollouts_left[slot])
                if assignments:
                    evaluator.load_slots(assignments)
                if not evaluator.active_slots:
                    break
                for result in evaluator.step():
                    slot = result["env_slot"]
                    print(f"Result: instance={result['instance_id']} rollout={result['rollout_id']} "
                          f"steps={result['steps']} success={result['success']} "
                          f"q_score={result.get('q_score', {}).get('final')}", flush=True)
                    rollouts_left[slot] -= 1
                    if rollouts_left[slot] == 0:
                        print(f"@@WORKER_OK {held.pop(slot)}", flush=True)
        except Exception:
            traceback.print_exc()
            for idx in held.values():
                print(f"@@WORKER_FAIL {idx}", flush=True)
            sys.exit(1)


if __name__ == "__main__":
    main()
