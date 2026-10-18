"""R1Pro trunk as the teleop's 2 DOF (translate, tilt).

The JoyLo teleop (BEHAVIOR-1K/joylo, SIMPLIFIED_TRUNK_CONTROL) never commands the four torso joints freely:
`translate` in [0, 2] moves along the keyframe path UPRIGHT -> DOWNWARD -> GROUND, and `tilt` is an offset on
torso_joint3 only (torso_joint4 is always 0). Every demo torso command is exactly compose(translate, tilt), and
the inverse is exact: translate from joint 1 (monotone path), tilt = q3 - path(translate)[2]. The path is
extrapolated linearly outside [0, 2], so both directions are exact inverses on all of R^2.

Model layout (21): [base 3][translate, tilt][left arm 7][left grip][right arm 7][right grip].
Env / dataset layout stays 23-dim with the 4 torso joints at 3:7.
"""

import numpy as np

# Keyframes from BEHAVIOR-1K/joylo/gello/utils/og_teleop_cfg.py (r1pro)
TORSO_UPRIGHT = np.array([0.45, -0.4, 0.0, 0.0])
TORSO_DOWNWARD = np.array([1.6, -2.5, -0.94, 0.0])
TORSO_GROUND = np.array([1.735, -2.57, -2.1, 0.0])
_SEG1 = TORSO_DOWNWARD - TORSO_UPRIGHT
_SEG2 = TORSO_GROUND - TORSO_DOWNWARD

# For each model dim, the env dim it copies (None for translate / tilt)
MODEL_TO_ENV_INDEX = [0, 1, 2, None, None] + list(range(7, 23))


def path_from_translate(t):
    t = np.asarray(t, dtype=np.float64)[..., None]
    return np.where(t <= 1.0, TORSO_UPRIGHT + t * _SEG1, TORSO_DOWNWARD + (t - 1.0) * _SEG2)


def decompose(torso):
    """Torso joints [..., 4] -> (translate, tilt) [..., 2]."""
    torso = np.asarray(torso, dtype=np.float64)
    q1 = torso[..., 0]
    t = np.where(q1 > TORSO_DOWNWARD[0], 1.0 + (q1 - TORSO_DOWNWARD[0]) / _SEG2[0], (q1 - TORSO_UPRIGHT[0]) / _SEG1[0])
    return np.stack([t, torso[..., 2] - path_from_translate(t)[..., 2]], axis=-1)


def compose(tt):
    """(translate, tilt) [..., 2] -> torso joints [..., 4], as the teleop emits them."""
    tt = np.asarray(tt, dtype=np.float64)
    q = path_from_translate(tt[..., 0])
    q[..., 2] += tt[..., 1]
    return q


def _dtype(x):
    return x.dtype if np.issubdtype(x.dtype, np.floating) else np.float32


def env_to_model(x):
    """[..., 23] env layout -> [..., 21] model layout."""
    x = np.asarray(x)
    return np.concatenate([x[..., :3], decompose(x[..., 3:7]), x[..., 7:]], axis=-1).astype(_dtype(x))


def model_to_env(x):
    """[..., 21] model layout -> [..., 23] env layout."""
    x = np.asarray(x)
    return np.concatenate([x[..., :3], compose(x[..., 3:5]), x[..., 5:]], axis=-1).astype(_dtype(x))
