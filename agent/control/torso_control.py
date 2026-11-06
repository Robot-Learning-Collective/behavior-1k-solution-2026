"""Absolute four-joint torso targets; native POSITION control remains authoritative."""
import numpy as np
from action_validation import InvalidAction

MAX_SLEW_RAD_PER_TICK = 0.025
CONTROL_HZ = 30.0


class ControllerFault(RuntimeError):
    """Expected controller infeasibility; stop the action, not the simulator."""
    def __init__(self, code, message, evidence):
        super().__init__(message)
        self.code, self.evidence = code, evidence

    def as_dict(self):
        return {'code': self.code, 'message': str(self), 'evidence': self.evidence,
                'recoverable': True, 'automatic_retry': False}


def validate_target(value, bounds):
    if (not isinstance(value, list) or len(value) != 4
            or any(type(v) not in (int, float) for v in value)):
        raise InvalidAction('torso_q needs four finite numeric radians (not bool/string)')
    q = np.asarray(value, dtype=float)
    if bounds is None:
        raise InvalidAction('Runtime torso limits required for torso_q')
    lo, hi = (np.asarray(v, dtype=float) for v in bounds)
    if (lo.shape != (4,) or hi.shape != (4,) or not np.isfinite([lo, hi]).all()
            or np.any(lo >= hi)):
        raise InvalidAction('Invalid runtime torso limits')
    if not np.isfinite(q).all() or np.any(q < lo) or np.any(q > hi):
        raise InvalidAction('torso_q outside finite runtime endpoint limits')
    return q.copy()


def slew_limits(velocity_limits):
    v = np.asarray(velocity_limits, dtype=float)
    if v.shape != (4,) or not np.isfinite(v).all() or np.any(v <= 0):
        raise ValueError('Expected four positive finite torso velocity limits')
    return np.minimum(MAX_SLEW_RAD_PER_TICK, v / CONTROL_HZ)


def bounded_target(desired, measured, previous_command, bounds, max_step):
    """Slew the previous POSITION command; measured tracking lag is not a cap.

    Actuator effort limits bound force. Measured remains an input for diagnostics
    and finite-state validation, never for re-anchoring or limiting the command.
    """
    desired, measured, previous_command, max_step = (
        np.asarray(v, dtype=float) for v in (desired, measured, previous_command, max_step))
    lo, hi = (np.asarray(v, dtype=float) for v in bounds)
    values = (desired, measured, previous_command, max_step, lo, hi)
    if any(v.shape != (4,) or not np.isfinite(v).all() for v in values):
        raise RuntimeError('Nonfinite/malformed torso runtime state')
    if np.any(max_step <= 0) or np.any(max_step > MAX_SLEW_RAD_PER_TICK):
        raise RuntimeError('Invalid torso runtime slew bound')
    lower = np.maximum(lo, previous_command - max_step)
    upper = np.minimum(hi, previous_command + max_step)
    if np.any(lower > upper):
        raise ControllerFault('torso_command_outside_limits',
                              'Previous torso command lies outside compatible joint/slew bounds',
                              {'joint_indices': np.flatnonzero(lower > upper).tolist(),
                               'desired_rad': desired.tolist(), 'measured_rad': measured.tolist(),
                               'previous_command_rad': previous_command.tolist(),
                               'max_step_rad': max_step.tolist(), 'lower_rad': lower.tolist(),
                               'upper_rad': upper.tolist()})
    return np.clip(desired, lower, upper)
