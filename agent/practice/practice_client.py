"""Practice binding around agent/control/sim_client.py: holds, a step-budget meter, layout switching, zero-shot.

A practice run's `sim_client.py` (written by bin/make_run.py) imports this module, so the agent's ordinary
`import sim_client as s` goes through it. It changes no control behaviour; it adds:

  holds         STOP or PRACTICE-HOLD in the run directory refuses every call (user stop, runtime blocker,
                WAIT_NEXT_INSTANCE). An act whose execution is uncertain writes PRACTICE-HOLD: no automatic replay.
  one caller    a file lock refuses concurrent robot calls from separate tool processes.
  budget meter  every state block ends with "steps used / official budget" (native 30 Hz).
  new layouts   the operator stages a new instance as SETUP.next.json; the agent's own next admin_reset switches
                to it (no session restart). With "zero_shot": true in that file, snapshots, restores and practice
                feedback are refused until admin_finish of that first attempt.
  events        every call is logged to practicer-events.jsonl (operation, sim time, ticks; no content).
"""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import time

RUN = Path(os.environ['BEHAVIOR_SIM_RUN_DIR']).resolve()
SETUP = RUN / 'SETUP.json'
HOLD = RUN / 'PRACTICE-HOLD'
ZERO_SHOT = RUN / 'ZERO-SHOT.json'
CLIENT = Path(__file__).resolve().parents[1] / 'control/sim_client.py'
STUDY = ('Zero-shot attempt failed. Now go back to the human proprio + RGB across DIFFERENT annotations in '
         'DIFFERENT episodes: compare the same fine-annotation segment across 2-3 demos, plus neighbouring '
         'segments, step through them densely (approach / pre-contact / contact / object-changing move / '
         'release), tabulate the human-vs-own differences in NOTES.md, change those, and retry (snapshots and '
         'practice feedback are allowed again).')
# Served through __getattr__ below, so `from sim_client import *` exports the robot API.
__all__ = ['observe', 'last_obs', 'xyz', 'pixel_to_body', 'act', 'admin_reset', 'admin_finish',
           'practice_feedback', 'snapshot', 'restore']
_client = None
_generation = None


def atomic(path, data):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def check_hold():
    for path in (RUN / 'STOP', HOLD):
        if path.exists():
            raise RuntimeError(f'Practice held: {path}; do not override user/runtime holds')


def meter(reply, setup):
    budget = setup['task_instance']['official_nominal_step_budget']
    seconds = reply.get('simulated_seconds')
    used = round(float(seconds) * 30) if seconds is not None else 'unknown'  # worker time is exactly steps / 30
    return f'  steps used / official budget: {used} / {budget} (native 30 Hz; practice meter, not a termination gate)'


def load_client(path=SETUP):
    """The control client bound to SETUP (or a staged SETUP.next.json); reloaded when the binding changes."""
    global _client, _generation
    setup = json.loads(path.read_text())
    generation = (setup.get('queue'), str(path))
    if setup.get('status') != 'READY':
        raise RuntimeError('Practice binding is not READY: ' + str(path))
    if _client is not None and generation == _generation:
        return _client
    os.environ['BEHAVIOR_SIM_SETUP_FILE'] = str(path)
    spec = importlib.util.spec_from_file_location('_practice_bound_client', CLIENT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    compact = module._compact_state
    module._compact_state = lambda reply, intent, failure=None: compact(reply, intent, failure) + '\n' + meter(reply, setup)
    _client, _generation = module, generation
    return module


def _reset(*args, **kwargs):
    """A staged layout is selected only here, at the agent's own reset."""
    check_hold()
    if kwargs.get('practice', True):
        kwargs['unbounded_practice'] = True  # the native step budget stays the agent's own target (meter)
    pending = RUN / 'SETUP.next.json'
    if not pending.exists() or json.loads(pending.read_text()).get('status') != 'READY':
        return load_client().admin_reset(*args, **kwargs)
    old, new = json.loads(SETUP.read_text()), json.loads(pending.read_text())
    if new['task_instance']['task'] != old['task_instance']['task']:
        raise RuntimeError('Staged slot is for another task; leave it untouched')
    stamp = str(time.time_ns())
    archive = RUN / f'SETUP.before-reset-{stamp}.json'
    archive.write_bytes(SETUP.read_bytes())
    receipt = RUN / f'reset-handoff-{stamp}.json'
    atomic(receipt, {'state': 'reset-dispatched', 'old_setup': str(archive), 'new_setup': new})
    try:
        result = load_client(pending).admin_reset(*args, **kwargs)
        if isinstance(result, tuple) and isinstance(result[1], dict) and result[1].get('error'):
            raise RuntimeError('Staged reset returned an error; see ' + str(receipt))
        if json.loads(pending.read_text()) != new:
            raise RuntimeError('Staged binding changed during reset; reset is not retried')
        atomic(SETUP, new)
        pending.rename(RUN / f'SETUP.consumed-{stamp}.json')
        os.environ['BEHAVIOR_SIM_SETUP_FILE'] = str(SETUP)
        atomic(receipt, {'state': 'switched', 'old_setup': str(archive), 'old_queue': old['queue'],
                         'new_queue': new['queue']})
        instance = new['task_instance'].get('native_instance_id')
        print('[SLOT_SWITCH] ' + str(receipt))
        if new.get('zero_shot'):
            atomic(ZERO_SHOT, {'instance': instance, 'switched_receipt': str(receipt)})
            print(f'[ZERO_SHOT] New unseen instance {instance}: this first attempt follows your NOTES EVAL PROCEDURE '
                  'only. No demo study, snapshots/restores or intermediate practice feedback until admin_finish; '
                  'its feedback is returned then.')
        return result
    except Exception:
        HOLD.write_text(f'Staged-slot reset outcome needs operator recovery; do not retry. See {receipt}\n')
        raise


def event(name, **data):
    with (RUN / 'practicer-events.jsonl').open('a') as stream:
        stream.write(json.dumps({'time': time.time(), 'event': name, **data}) + '\n')


def invoke(name, *args, **kwargs):
    check_hold()
    with (RUN / '.practice-call.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        client = None if name == 'admin_reset' else load_client()
        if ZERO_SHOT.exists() and name in ('snapshot', 'restore', 'practice_feedback'):
            raise RuntimeError('Zero-shot attempt on a new instance: snapshots, restores and intermediate feedback '
                               'are unavailable until admin_finish')
        try:
            result = _reset(*args, **kwargs) if name == 'admin_reset' else getattr(client, name)(*args, **kwargs)
            if name == 'admin_finish' and ZERO_SHOT.exists():
                zero = json.loads(ZERO_SHOT.read_text())
                success = bool((result or {}).get('practice_feedback', {}).get('success'))
                ZERO_SHOT.rename(RUN / f"zero-shot-{zero['instance']}-{'success' if success else 'failed'}.json")
                event('zero_shot_finished', instance=zero['instance'], success=success)
                print('[ZERO_SHOT_DONE] success; record it in NOTES and keep practising.' if success
                      else '[ZERO_SHOT_DONE] ' + STUDY)
            public = result if isinstance(result, dict) else {}
            event('sim_call', operation=name, simulated_seconds=public.get('simulated_seconds'),
                  executed_ticks=(public.get('execution') or {}).get('executed_ticks'),
                  observation_id=public.get('observation_id'))
        except Exception as error:
            event('sim_error', operation=name, error_type=type(error).__name__)
            raise
        finally:
            if name == 'act' and client is not None and client.STATE_CACHE.exists():
                if json.loads(client.STATE_CACHE.read_text()).get('motion_execution_uncertain'):
                    HOLD.write_text('Uncertain action; no automatic replay, observe or reset. Ask the operator.\n')
        return result


def admin_reset(*args, **kwargs):
    return invoke('admin_reset', *args, **kwargs)


def main():
    """CLI (`python3 sim_client.py observe|act|pixel ...`), routed through invoke() like Python calls."""
    import argparse
    parser = argparse.ArgumentParser(description='Practice robot client: observe, pixel measurement or one act')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('observe').add_argument('--intent', default='Observe scene')
    commands.add_parser('act').add_argument('json', help='e.g. {"right":{"up":0.02}}')
    pixel = commands.add_parser('pixel')
    pixel.add_argument('camera', choices=['left', 'head', 'right'])
    pixel.add_argument('u', type=float)
    pixel.add_argument('v', type=float)
    args = parser.parse_args()
    if args.command == 'observe':
        invoke('observe', args.intent)
    elif args.command == 'pixel':
        point = invoke('pixel_to_body', args.camera, args.u, args.v)
        print(json.dumps([float(x) if x == x else None for x in point]))
    else:
        params = json.loads(args.json)
        if not isinstance(params, dict):
            parser.error('act JSON must be an object')
        invoke('act', **params)


def __getattr__(name):
    if name.startswith('__'):
        raise AttributeError(name)
    attr = getattr(load_client(), name)
    if callable(attr) and not name.startswith('_'):
        return lambda *args, **kwargs: invoke(name, *args, **kwargs)
    return attr
