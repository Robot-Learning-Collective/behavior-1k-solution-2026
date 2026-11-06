"""Offline BODY FK/DLS candidate search; no simulator calls or collision checking."""
import numpy as np
from robot_kinematics import RobotModel, rotation_error


def solve(arm, torso, position, finger, close, measured, lower, upper, seeds=24):
    model = RobotModel()
    finger = np.asarray(finger, float)
    finger /= np.linalg.norm(finger)
    close = np.asarray(close, float)
    close -= np.dot(close, finger) * finger
    close /= np.linalg.norm(close)
    desired = np.column_stack((np.cross(close, finger), close, finger))
    lower, upper = np.asarray(lower) + .01, np.asarray(upper) - .01
    rng = np.random.default_rng(7)
    found = []
    for i in range(seeds):
        q = np.clip(measured if i == 0 else rng.uniform(lower, upper), lower, upper)
        for _ in range(350):
            p, rotation, jac = model.arm(arm, torso, q)
            dp = np.asarray(position) - p
            dr = rotation_error(desired, rotation)
            if np.linalg.norm(dp) < .002 and np.linalg.norm(dr) < .015:
                found.append((float(np.linalg.norm(q - measured)), q.copy(), p, rotation))
                break
            error = np.r_[dp, .25 * dr]
            jac = jac.copy()
            jac[3:] *= .25
            dq = jac.T @ np.linalg.solve(jac @ jac.T + .003**2 * np.eye(6), error)
            dq *= min(1., .15 / max(np.linalg.norm(dq), 1e-12))
            q = np.clip(q + dq, lower, upper)
    return sorted(found, key=lambda item: item[0])
