"""Public-client wrapper for fresh-reset, step-budgeted patio practice.

Use the authorized unbounded-practice lifecycle to avoid a separate legacy wall
horizon, but cap EVERY act at the remaining official 18106 native ticks.
No snapshot restores in a full-reset result. This is not an official evaluator.
"""
import sim_client as _sim
from sim_client import *

STEP_BUDGET = 18106


def act(**kwargs):
    obs = _sim.last_obs()
    if not obs['attempt_id'].startswith('patio-speed-'):
        raise ValueError('Budget wrapper requires a patio-speed-* attempt')
    used = round(float(obs['simulated_seconds']) * 30)
    remaining = STEP_BUDGET - used
    if remaining <= 0:
        raise RuntimeError(f'Official step budget exhausted: {used}/{STEP_BUDGET}')
    requested = kwargs.get('max_steps')
    kwargs['max_steps'] = remaining if requested is None else min(requested, remaining)
    return _sim.act(**kwargs)
