"""Hybrid arm control: 6D BODY Cartesian delta (with nullspace elbow-down DLS), 7D joint POSITION target, named preset, or dict with delta+bias."""
import numpy as np
from action_validation import validate as validate_strict6, InvalidAction
from joint_action import target as joint_target
from torso_control import validate_target as validate_torso_target

SLEW_RAD_PER_TICK = 0.025
MAX_TRANS_NORM = 0.30
MAX_ROT_NORM = 1.20

# Human-demonstrated elbow-down nominal postures (radians) that keep elbows down,
# away from hard limits, and clear of the head camera.
Q_NOMINAL = {
    'left':  np.array([-0.26, -0.08,  0.05, -1.30,  0.00,  0.12,  0.05], dtype=float),
    'right': np.array([-0.35,  0.05, -0.08, -1.10,  0.00,  0.10, -0.10], dtype=float),
}

# Verified human-demonstration postures (all strictly inside endpoint_lower_rad..endpoint_upper_rad)
PRESETS = {
    'left': {
        'tuck':            np.array([-0.066, -0.118,  0.315, -1.521,  0.353,  0.162,  0.084], dtype=float),
        'ready':           np.array([-0.260, -0.100,  0.050, -1.340, -0.050,  0.050,  0.040], dtype=float),
        'box_approach':    np.array([-0.560, -0.010,  0.400, -0.880,  0.320,  0.440,  0.200], dtype=float),
        'box_carry':       np.array([ 0.040, -0.155,  0.510, -1.520,  0.510,  0.250,  0.090], dtype=float),
        'push_top':        np.array([-0.260, -0.109,  0.031, -1.338, -0.110, -0.039,  0.031], dtype=float),
        'push_top_above':  np.array([-0.255, -0.109,  0.032, -1.338, -0.110, -0.029,  0.032], dtype=float),
        'push_top_press':  np.array([-0.265, -0.106,  0.043, -1.250, -0.116,  0.174,  0.035], dtype=float),
        'push_top_pull':   np.array([ 0.248, -0.101,  0.053, -1.513, -0.171, -0.328,  0.074], dtype=float),
        'pinch_top':       np.array([ 0.283, -0.109, -0.035, -1.509, -1.611,  0.097,  0.288], dtype=float),
        'pinch_top_open':  np.array([ 0.283, -0.109, -0.035, -1.509, -1.611,  0.097,  0.288], dtype=float),
        'pinch_top_eng':   np.array([ 0.283, -0.109, -0.034, -1.506, -1.614,  0.104,  0.486], dtype=float),
        'pinch_top_lift':  np.array([ 0.222, -0.109, -0.034, -1.318, -1.612,  0.101,  1.459], dtype=float),
        'push_mid':        np.array([-0.480, -0.155,  0.244, -0.928, -0.354, -0.101,  0.048], dtype=float),
        'push_mid_above':  np.array([-0.481, -0.155,  0.123, -1.077, -0.384,  0.132,  0.055], dtype=float),
        'push_mid_press':  np.array([-0.482, -0.155,  0.122, -1.008, -0.431,  0.290,  0.090], dtype=float),
        'push_mid_pull':   np.array([-0.090, -0.155,  0.023, -1.338, -0.104, -0.060,  0.094], dtype=float),
        'pinch_mid':       np.array([-0.084, -0.065,  0.180, -0.995,  1.331,  0.137, -0.790], dtype=float),
        'pinch_mid_open':  np.array([-0.084, -0.101,  0.180, -1.040,  1.333,  0.134, -0.431], dtype=float),
        'pinch_mid_eng':   np.array([-0.084, -0.065,  0.178, -0.994,  1.324,  0.138, -0.784], dtype=float),
        'pinch_mid_lift':  np.array([-0.081,  0.561,  0.606, -0.954,  0.403,  0.135, -1.216], dtype=float),
        'hold_side':       np.array([ 0.215,  0.294,  1.245, -0.337, -0.883, -0.204,  0.990], dtype=float),
        'carry_book':      np.array([-0.281, -0.129,  0.042, -1.523,  0.008,  0.346,  0.234], dtype=float),
        'place_box':       np.array([-0.278, -0.131, -0.446, -0.952, -1.284,  0.508, -0.228], dtype=float),
    },
    'right': {
        'tuck':            np.array([-0.078,  0.099, -0.290, -1.549, -0.004,  0.147, -0.033], dtype=float),
        'ready':           np.array([-0.350,  0.050, -0.080, -1.100,  0.000,  0.050, -0.100], dtype=float),
        'box_approach':    np.array([-0.943,  0.012,  0.030, -0.395, -0.022,  0.756, -0.036], dtype=float),
        'box_grasp':       np.array([-0.897,  0.006,  0.036, -0.511, -0.018,  0.434, -0.028], dtype=float),
        'box_carry':       np.array([-0.554,  0.004,  0.014, -0.498, -0.027,  0.036, -0.033], dtype=float),
        'box_place':       np.array([-0.770,  0.010,  0.010, -0.370, -0.020,  0.885, -0.035], dtype=float),
        'push_top':        np.array([-0.412,  0.066, -0.038, -1.021, -0.046, -0.106, -0.149], dtype=float),
        'push_top_above':  np.array([-0.407,  0.066, -0.041, -1.131,  0.146, -0.038, -0.156], dtype=float),
        'push_top_press':  np.array([-0.412,  0.067, -0.043, -0.961,  0.153, -0.043, -0.154], dtype=float),
        'push_top_pull':   np.array([ 0.115,  0.097, -0.100, -1.381,  0.211, -0.371, -0.145], dtype=float),
        'pinch_top':       np.array([-0.018,  0.074, -0.222, -1.260, -1.446,  0.154,  0.233], dtype=float),
        'pinch_top_open':  np.array([-0.034,  0.063, -0.226, -1.222, -1.451,  0.172,  0.238], dtype=float),
        'pinch_top_eng':   np.array([-0.034,  0.046, -0.231, -1.075, -1.443,  0.188,  0.734], dtype=float),
        'pinch_top_lift':  np.array([-0.310, -0.224,  0.062, -0.951, -0.244, -0.272,  1.513], dtype=float),
        'push_mid':        np.array([-0.355,  0.020, -0.149, -1.024,  0.523, -0.305, -0.268], dtype=float),
        'push_mid_above':  np.array([-0.338,  0.026, -0.058, -1.046,  0.507, -0.267, -0.265], dtype=float),
        'push_mid_press':  np.array([-0.336,  0.028, -0.068, -0.981,  0.546, -0.256, -0.266], dtype=float),
        'push_mid_pull':   np.array([-0.074,  0.065, -0.062, -1.181,  0.489, -0.448, -0.269], dtype=float),
        'pinch_mid':       np.array([-0.194, -0.044, -0.112, -0.743, -1.498,  0.187,  0.965], dtype=float),
        'pinch_mid_open':  np.array([-0.194, -0.042, -0.112, -0.843, -1.495,  0.187,  0.605], dtype=float),
        'pinch_mid_eng':   np.array([-0.194, -0.044, -0.112, -0.756, -1.498,  0.186,  0.934], dtype=float),
        'pinch_mid_lift':  np.array([-0.263, -0.288,  0.089, -1.043, -0.319, -0.178,  1.451], dtype=float),
        'carry_book':      np.array([-0.316,  0.044,  0.070, -1.541, -0.082,  0.170, -0.252], dtype=float),
        'place_box':       np.array([-0.640,  0.015,  0.007, -0.947, -0.069,  0.999,  0.349], dtype=float),
    },
}


def _resolve_bias(arm, bias_spec, bounds):
    if bias_spec is None:
        return None
    lo, hi = bounds[arm]
    if isinstance(bias_spec, str):
        if bias_spec not in PRESETS[arm]:
            raise InvalidAction(f'Unknown {arm} bias preset {bias_spec!r}')
        return np.clip(PRESETS[arm][bias_spec].copy(), lo, hi)
    if isinstance(bias_spec, list) and len(bias_spec) == 7 and all(type(v) in (int, float) for v in bias_spec):
        arr = np.asarray(bias_spec, dtype=float)
        if np.isfinite(arr).all() and np.all(arr >= lo) and np.all(arr <= hi):
            return arr.copy()
    raise InvalidAction(f'Invalid {arm} bias specification')


def resolve_arm_spec(arm, spec, bounds):
    """
    Validates and normalizes `command[arm]` into one of:
      - ('hold', None)
      - ('joint7', np.ndarray(7,))
      - ('cartesian6', {'delta': np.ndarray(6,), 'q_bias': np.ndarray(7,) | None})
    """
    lo, hi = bounds[arm]
    if spec is None:
        return ('hold', None)
    if isinstance(spec, str):
        if spec not in PRESETS[arm]:
            raise InvalidAction(f'Unknown {arm} preset {spec!r}; valid: {sorted(PRESETS[arm])}')
        q = np.clip(PRESETS[arm][spec].copy(), lo, hi)
        return ('joint7', q)
    if isinstance(spec, dict):
        if 'delta' not in spec or not set(spec).issubset({'delta', 'bias'}):
            raise InvalidAction(f'{arm} dict spec requires delta and optional bias')
        mode, payload = resolve_arm_spec(arm, spec['delta'], bounds)
        if mode == 'hold' and isinstance(spec['delta'], list) and len(spec['delta']) == 6:
            # Explicit delta dict retains Cartesian intent even at zero error.
            mode, payload = 'cartesian6', {'delta': np.zeros(6), 'q_bias': None}
        if mode != 'cartesian6':
            raise InvalidAction(f'{arm} dict delta must be 6D BODY delta')
        payload['q_bias'] = _resolve_bias(arm, spec.get('bias'), bounds)
        return ('cartesian6', payload)
    if isinstance(spec, list):
        if any(type(v) not in (int, float) for v in spec):
            raise InvalidAction(f'{arm} list elements must be finite numbers (not bool/string)')
        arr = np.asarray(spec, dtype=float)
        if not np.isfinite(arr).all():
            raise InvalidAction(f'{arm} must be finite')
        if len(arr) == 6:
            if np.linalg.norm(arr[:3]) > MAX_TRANS_NORM or np.linalg.norm(arr[3:]) > MAX_ROT_NORM:
                raise InvalidAction(f'{arm} exceeds BODYtranslation0.3m/rotation1.2rad norms')
            if not np.any(arr):
                return ('hold', None)
            return ('cartesian6', {'delta': arr, 'q_bias': None})
        if len(arr) == 7:
            if np.any(arr < lo) or np.any(arr > hi):
                raise InvalidAction(f'{arm} 7D joint target outside published endpoint limits')
            return ('joint7', arr.copy())
        raise InvalidAction(f'{arm} list must have length 6 (BODY delta) or 7 (joint target rad)')
    raise InvalidAction(f'{arm} must be None, 6D list, 7D list, preset string, or delta+bias dict')


def validate_command(command, bounds, torso_bounds=None):
    """Validates hybrid command (allowing 6D delta, 7D joint target, preset string, or None per arm)."""
    if not isinstance(command, dict):
        raise InvalidAction('Action must be a dictionary')
    expected = {'seconds', 'left', 'right', 'left_gripper', 'right_gripper', 'base', 'torso_delta'}
    if set(command) not in (expected, expected | {'torso_q'}):
        raise InvalidAction('Unknown/missing action fields')
    resolved = {}
    dummy = dict(command)
    if 'torso_q' in command:
        validate_torso_target(dummy.pop('torso_q'), torso_bounds)
    for arm in ('left', 'right'):
        resolved[arm] = resolve_arm_spec(arm, command[arm], bounds)
        dummy[arm] = None
    ticks = validate_strict6(dummy)
    if 'torso_q' in command and any(command['torso_delta']):
        raise InvalidAction('torso_q requires torso_delta=[0,0]; mixed torso modes rejected')
    return ticks, resolved


def nullspace_dls_step(jac, error, q_curr, lo, hi, arm, q_bias=None, max_step=SLEW_RAD_PER_TICK):
    """
    7-DOF DLS IK step with task-consistent nullspace posture & joint-limit avoidance.
    When q_bias is None, only proximal/elbow joints (0..3) are regularized toward Q_NOMINAL[arm][:4]
    so intentional wrist rolls (joints 4..6) are preserved while preventing elbow-up flip and singularities.
    Nullspace step is bounded to available slew headroom so primary 6D Cartesian tracking is never clipped.
    q_curr is the PREVIOUS COMMANDED configuration, not measured joints.
    Jacobian/error must refer to that same commanded model configuration.
    Returns (dq_unclipped, target_q_clipped) respecting command slew and [lo, hi].
    """
    n = len(q_curr)
    margin = 0.04
    grad_limit = np.zeros(n, dtype=float)

    for i in range(n):
        d_low = q_curr[i] - lo[i]
        d_high = hi[i] - q_curr[i]
        if d_low < margin:
            r = max(0.0, (margin - d_low) / margin)
            grad_limit[i] += 0.40 * (r * r)
        if d_high < margin:
            r = max(0.0, (margin - d_high) / margin)
            grad_limit[i] -= 0.40 * (r * r)

    j_pinv = jac.T @ np.linalg.solve(jac @ jac.T + 0.003 * np.eye(6), np.eye(6))
    dq_primary = j_pinv @ error

    dq_posture = grad_limit.copy()
    if q_bias is not None:
        q_nom = np.asarray(q_bias, dtype=float)
        dq_posture += 0.25 * (q_nom - q_curr)
    else:
        q_nom = Q_NOMINAL[arm]
        dq_posture[:4] += 0.25 * (q_nom[:4] - q_curr[:4])

    # Strong elbow-down flexion bias when near straight-arm singularity (joint4 > -0.60 rad)
    if q_curr[3] > -0.60:
        dq_posture[3] += 0.60 * (-1.15 - q_curr[3])

    null_proj = np.eye(n) - (j_pinv @ jac)
    dq_null = null_proj @ dq_posture
    max_null_slew = 0.018 if q_curr[3] > -0.60 else 0.004
    null_inf = float(np.max(np.abs(dq_null)))
    if null_inf > max_null_slew and null_inf > 1e-12:
        dq_null = dq_null * (max_null_slew / null_inf)

    dq = dq_primary + dq_null
    target = np.clip(q_curr + np.clip(dq, -np.asarray(max_step), max_step), lo, hi)
    return dq, target
