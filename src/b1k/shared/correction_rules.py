"""Gripper correction rule for BEHAVIOR-1K rollouts.

In the demos a gripper is fully closed only in a few (task, side, stage) cases (pressing a button or
switch); assets/semantic_stages/gripper_close_allowed.json lists them, from a scan of all 20k demos.
A gripper found fully closed anywhere else closed on air: the predicted chunk is replaced by the current
state with that gripper opened.
"""

import json
import logging
import pathlib

import numpy as np

logger = logging.getLogger(__name__)

# Gripper state in [-1, 1] (raw width [0, 0.1]); below this the gripper is fully closed
CLOSED_THRESHOLD = -0.98
GRIPPER_IDX = {"left": 14, "right": 22}

_ALLOWED_PATH = pathlib.Path(__file__).resolve().parents[3] / "assets" / "semantic_stages" / "gripper_close_allowed.json"
CLOSE_ALLOWED = {int(t): v for t, v in json.loads(_ALLOWED_PATH.read_text())["allow"].items()}


def gripper_open_correction(task_id: int, stage: int, state: np.ndarray, actions: np.ndarray) -> np.ndarray:
    """state: 23-dim current state; actions: (horizon, 23) predicted chunk."""
    sides = [
        side for side, idx in GRIPPER_IDX.items()
        if state[idx] < CLOSED_THRESHOLD and stage not in CLOSE_ALLOWED.get(task_id, {}).get(side, [])
    ]
    if not sides:
        return actions
    logger.info(f"🔧 GRIPPER CORRECTION: task {task_id}, stage {stage}: opening {sides}")
    corrected = np.tile(state, (actions.shape[0], 1))
    for side in sides:
        corrected[:, GRIPPER_IDX[side]] = 1.0
    return corrected
