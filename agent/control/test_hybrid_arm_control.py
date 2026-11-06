"""Offline unit tests for hybrid_arm_control.py and worker.py integration."""
import ast
from pathlib import Path
import numpy as np
from action_validation import InvalidAction
from hybrid_arm_control import (
    PRESETS,
    Q_NOMINAL,
    SLEW_RAD_PER_TICK,
    nullspace_dls_step,
    resolve_arm_spec,
    validate_command,
)

BOUNDS = {
    'left': (
        np.array([-4.4406, -0.1645, -2.3462, -2.0844, -2.3462, -1.0372, -1.5608]),
        np.array([ 1.2990,  3.1316,  2.3462,  0.3391,  2.3462,  1.0372,  1.5608]),
    ),
    'right': (
        np.array([-4.4406, -3.1316, -2.3462, -2.0844, -2.3462, -1.0372, -1.5608]),
        np.array([ 1.2990,  0.1645,  2.3462,  0.3391,  2.3462,  1.0372,  1.5608]),
    ),
}


def test_presets_within_bounds():
    for arm in ('left', 'right'):
        lo, hi = BOUNDS[arm]
        assert np.all(Q_NOMINAL[arm] >= lo) and np.all(Q_NOMINAL[arm] <= hi)
        for name, q in PRESETS[arm].items():
            assert q.shape == (7,), f'{arm}.{name} wrong shape'
            assert np.all(q >= lo) and np.all(q <= hi), f'{arm}.{name} out of bounds: {q}'
            mode, resolved = resolve_arm_spec(arm, name, BOUNDS)
            assert mode == 'joint7' and np.allclose(resolved, q)


def test_validate_command_modes_and_bounds():
    base_cmd = {
        'seconds': 1.5,
        'left': None,
        'right': None,
        'left_gripper': 1.0,
        'right_gripper': 0.0,
        'base': [0.0, 0.0, 0.0],
        'torso_delta': [0.0, 0.0],
    }
    ticks, res = validate_command(base_cmd, BOUNDS)
    assert ticks == 45 and res['left'][0] == 'hold' and res['right'][0] == 'hold'

    # Zero 6D delta also resolves to hold
    _, res0 = validate_command({**base_cmd, 'left': [0.0]*6}, BOUNDS)
    assert res0['left'][0] == 'hold'

    # Non-zero 6D delta resolves to cartesian6
    _, res6 = validate_command({**base_cmd, 'left': [0.15, 0.05, 0.10, 0.0, -0.3, 0.0]}, BOUNDS)
    assert res6['left'][0] == 'cartesian6'

    # 7D target resolves to joint7
    q7 = PRESETS['right']['pinch_top'].tolist()
    _, res7 = validate_command({**base_cmd, 'right': q7}, BOUNDS)
    assert res7['right'][0] == 'joint7' and np.allclose(res7['right'][1], q7)

    # Preset string resolves to joint7
    _, resp = validate_command({**base_cmd, 'left': 'pinch_top', 'right': 'box_grasp'}, BOUNDS)
    assert resp['left'][0] == 'joint7' and resp['right'][0] == 'joint7'

    # Reject invalid inputs (NaN, out-of-bounds 6D norm, out-of-bounds 7D joint, unknown preset, bad length)
    bad_inputs = [
        {'left': [0.31, 0, 0, 0, 0, 0]},
        {'right': [0, 0, 0, 1.25, 0, 0]},
        {'left': [0, 0, 0, 0, 0, float('nan')]},
        {'left': [0.0, -0.20, 0.0, -1.0, 0.0, 0.0, 0.0]},  # q2 < -0.1645 for left arm
        {'right': [0.0, 0.20, 0.0, -1.0, 0.0, 0.0, 0.0]},  # q2 > +0.1645 for right arm
        {'left': 'nonexistent_preset'},
        {'left': [1, 2, 3]},
        {'left': [True, 0, 0, 0, 0, 0]},
    ]
    for patch in bad_inputs:
        try:
            validate_command({**base_cmd, **patch}, BOUNDS)
        except InvalidAction:
            pass
        else:
            raise AssertionError(f'Accepted invalid input: {patch}')


def test_nullspace_dls_step_singularity_and_slew():
    lo, hi = BOUNDS['left']
    # At q = 0 (reset straight-arm singularity), test that nullspace bias bends joint4 negative
    # while respecting 0.025 rad/tick slew and [lo, hi] bounds.
    q = np.zeros(7, dtype=float)
    # Construct a rank-deficient / near-singular Jacobian with a nullspace on joint4 and joint3
    jac = np.eye(6, 7, dtype=float)
    jac[:, 3] = 0.0  # joint4 in nullspace of toy Jacobian to verify nullspace projection
    error = np.array([0.05, 0.0, 0.02, 0.0, 0.0, 0.0])

    for _ in range(40):
        dq, q_next = nullspace_dls_step(jac, error, q, lo, hi, 'left')
        assert np.all(np.isfinite(dq)) and np.all(np.isfinite(q_next))
        assert np.max(np.abs(q_next - q)) <= SLEW_RAD_PER_TICK + 1e-12
        assert np.all(q_next >= lo) and np.all(q_next <= hi)
        q = q_next

    assert q[3] < -0.5, f'Expected elbow joint4 to flex negative in nullspace, got {q[3]}'

    # Also verify that when wrist joint5 is rolled (e.g. -1.61 rad for vertical pinch) and q_bias is None,
    # nullspace_dls_step does not unwind joint5 toward 0 when joint5 is in the nullspace.
    q_pinch = PRESETS['left']['pinch_top_open'].copy()
    jac_wrist = np.eye(6, 7, dtype=float)
    jac_wrist[:, 4] = 0.0  # joint5 in nullspace
    _, q_pinch_next = nullspace_dls_step(jac_wrist, np.zeros(6), q_pinch, lo, hi, 'left', q_bias=None)
    assert abs(q_pinch_next[4] - q_pinch[4]) < 1e-9, f'Expected wrist roll q5 to be preserved, got {q_pinch_next[4]} vs {q_pinch[4]}'


def test_worker_ast_syntax():
    worker_path = Path(__file__).resolve().parents[1] / 'practice/worker.py'
    tree = ast.parse(worker_path.read_text())
    assert any(isinstance(n, ast.FunctionDef) and n.name == 'main' for n in tree.body)


if __name__ == '__main__':
    test_presets_within_bounds()
    test_validate_command_modes_and_bounds()
    test_nullspace_dls_step_singularity_and_slew()
    test_worker_ast_syntax()
    print('HYBRID_ARM_CONTROL_AND_NULLSPACE_DLS_ALL_TESTS_PASS')
