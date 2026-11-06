"""Agent route: GPT-6 Astra plays the tasks enabled in agent/tasks/tasks.json; other tasks stay on the
learned policy. See agent/README.md for the whole design.

One AgentRoute per evaluator connection. Each episode (evaluator reset) starts undecided:
its first observation selects the agent (enabled task, one environment, full-resolution RGBD,
OpenAI API reachable) or the base policy. If the agent is slow to answer, the robot is held
still and the route keeps waiting; after MAX_QUERY_TIMEOUTS consecutive timeouts, or on any
agent failure (missing key, API/provider error, cost guard, wall budget, ...), the rest of that
episode is played by the base policy, with red errors in the log. The next reset always starts
a fresh agent attempt. No chunk replay, no action replay.
"""
import concurrent.futures
import json
import logging
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request
import uuid

import numpy as np

PROPRIO_KEY = 'robot_r1::proprio'
DEFAULT_MODEL = 'openai/gpt-6-astra'
REPO = Path(__file__).resolve().parents[3]
AGENT_ROOT = REPO / 'agent'
REGISTRY = AGENT_ROOT / 'tasks/tasks.json'
# Pi extensions every agent episode loads: spend cap and keeping the API key out of tool subprocesses.
GUARD_EXTENSIONS = ('pi/extensions/cost-guard.ts', 'pi/extensions/auth-isolation.ts')
# The evaluator allows 600 s for the first query of an episode (2026/eval); answer (hold or
# fallback step, incl. a possible model compile) well inside it. Later queries: 570 s.
FIRST_QUERY_LIMIT_S = 540.0
QUERY_LIMIT_S = 570.0
# Consecutive query timeouts (each answered with a hold action) before the base policy takes over.
MAX_QUERY_TIMEOUTS = 3
# The frozen runtime's per-call watchdog; above the bridge's own 599 s goal wait, which
# ends a call cleanly so that the route can re-issue it with the newest observation.
RUNTIME_QUERY_LIMIT_S = 630
BRIDGE_WAIT_TIMEOUT = 'Waiting for agent exceeded query/episode wall budget'
FALLBACK_REMINDER_STEPS = 300

RED, RESET = '\033[1;31m', '\033[0m'


def alarm(*lines):
    """Loud, red, multi-line error for the container log."""
    bar = '!' * 100
    for line in (bar, *lines, bar):
        logging.error(f'{RED}{line}{RESET}')


def _mask(text):
    return re.sub(r'sk-[A-Za-z0-9_*\-]+', 'sk-***', str(text))


def agent_model(entry=None):
    return os.environ.get('B1K_AGENT_MODEL') or (entry or {}).get('model') or DEFAULT_MODEL


def load_enabled_tasks(registry=REGISTRY):
    """{official task id: entry} for every enabled task; entries carry the registry defaults."""
    data = json.loads(Path(registry).read_text())
    defaults = data.get('defaults', {})
    return {entry['task_id']: {**defaults, 'task_name': name, **entry}
            for name, entry in data['tasks'].items() if entry.get('enabled')}


def missing_contexts(tasks):
    """Task names whose frozen practice session is not on disk (see agent/eval/frozen.py)."""
    return sorted(entry['task_name'] for entry in tasks.values()
                  if not (AGENT_ROOT / 'tasks' / entry['task_name'] / 'session.jsonl').is_file())


_PROFILE = None
_FINGER_LIMITS = None


def _profile():
    global _PROFILE
    if _PROFILE is None:
        _PROFILE = json.loads((AGENT_ROOT / 'control/static-profile.json').read_text())
    return _PROFILE


def camera_problem(obs):
    """None if the observation is the official full-resolution RGBD (RGBDFullResWrapper)."""
    profile, problems = _profile(), []
    if profile['robot_name'] + '::cam_rel_poses' not in obs:
        problems.append('no camera poses')
    for name in profile['camera_order']:
        meta = profile['cameras'][name]
        expected = tuple(meta['image_size_hw'])
        rgb = obs.get(meta['observation_prefix'] + '::rgb')
        depth = obs.get(meta['observation_prefix'] + '::depth_linear')
        shape = None if rgb is None else tuple(np.shape(rgb))[-3:-1]
        if shape != expected:
            problems.append(f'{name} RGB {shape}, expected {expected}')
        if depth is None:
            problems.append(f'{name} has no depth')
    if not problems:
        return None
    return ('observations are not the official full-resolution RGBD (RGBDFullResWrapper: 720x720 head, '
            '480x480 wrists, depth): ' + '; '.join(problems))


def hold_action(obs, last_action=None):
    """Native 23-dim action that keeps the robot where it is (base stopped).

    Repeats the controller's last command (its terminal hold while the agent plans);
    before the first command, holds the measured joints and gripper openings.
    """
    if last_action is not None:
        action = np.array(last_action, dtype=np.float32).reshape(23).copy()
        action[:3] = 0.0
        return action
    global _FINGER_LIMITS
    if _FINGER_LIMITS is None:
        joints = json.loads((AGENT_ROOT / 'control/robot_model.json').read_text())['joints']
        _FINGER_LIMITS = {j['name']: (j['limits']['lower'], j['limits']['upper']) for j in joints
                          if 'gripper_finger_joint' in j['name']}
    q = np.asarray(obs[PROPRIO_KEY], dtype=np.float64).reshape(-1)[:61]
    action = np.zeros(23, dtype=np.float32)
    action[3:7] = q[53:57]
    for arm, start, out in (('left', 3, 7), ('right', 28, 15)):
        action[out:out + 7] = q[start:start + 7]
        opening = []
        for i, position in enumerate(q[start + 21:start + 23], 1):
            lower, upper = _FINGER_LIMITS[f'{arm}_gripper_finger_joint{i}']
            opening.append((position - lower) / max(upper - lower, 1e-9))
        action[out + 7] = 2 * float(np.clip(np.mean(opening), 0.0, 1.0)) - 1
    return action


def api_preflight(model, timeout=20.0, attempts=2):
    """One tiny model request (a few tokens, ~$0.001 or less). Returns (ok, message).

    Checks key, model access, quota and network in one go. Only the OpenAI API-key
    provider is checked; other providers (e.g. OAuth) report 'not checked'.
    """
    provider, _, name = model.partition('/')
    if provider != 'openai':
        return True, f'not checked (provider {provider})'
    key = os.environ.get('OPENAI_API_KEY', '').strip()
    if not key:
        return False, 'OPENAI_API_KEY is not set in the container'
    request = urllib.request.Request(
        'https://api.openai.com/v1/responses',
        data=json.dumps({'model': name, 'input': 'Reply with OK.', 'max_output_tokens': 16,
                         'store': False}).encode(),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    message = 'not attempted'
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return True, f'model {name} answered (HTTP {response.status})'
        except urllib.error.HTTPError as error:
            try:
                detail = json.loads(error.read()).get('error') or {}
                message = (f"HTTP {error.code} {detail.get('code') or detail.get('type') or ''}: "
                           f"{detail.get('message') or ''}")
            except Exception:
                message = f'HTTP {error.code}'
            if error.code not in (408, 409, 429, 500, 502, 503, 504):
                break
        except Exception as error:
            message = f'{type(error).__name__}: {error}'
        if attempt + 1 < attempts:
            time.sleep(3)
    return False, _mask(message)


def startup_check(tasks):
    """Run once at server start, before the policy loads. Returns True when the agent's API works.

    On failure it prints a loud red explanation; the caller then stops the container instead of
    serving, so a broken key or network is noticed before any episode runs.
    """
    if not tasks:
        return True
    names = sorted(entry.get('task_name', str(task)) for task, entry in tasks.items())
    missing = missing_contexts(tasks)
    if missing:
        alarm('STARTUP FAILED: FROZEN PRACTICE CONTEXTS ARE MISSING. THE POLICY SERVER IS NOT RUNNING.',
              f'No session.jsonl for: {", ".join(missing)}.',
              'Assemble them with `python -m agent.eval.frozen` (see agent/README.md), or start without --agent.')
        return False
    for model in sorted({agent_model(entry) for entry in tasks.values()}):
        ok, message = api_preflight(model)
        if ok:
            logging.info(f'Agent API check passed: {model}: {message}')
            continue
        if not os.environ.get('OPENAI_API_KEY', '').strip():
            advice = ['OPENAI_API_KEY is not set. Pass it at runtime (docker run --env-file ...).']
        elif message.startswith('HTTP 4'):
            advice = ['The OpenAI API was reached but rejected the key or request (see Reason).']
        else:
            advice = ['Make sure the server can reach api.openai.com over HTTPS, then start it again.']
        alarm('STARTUP FAILED: THE OPENAI CHECK DID NOT PASS. THE POLICY SERVER IS NOT RUNNING.',
              f'Reason: {message}',
              f'Model {model} is needed for {len(names)} tasks: {", ".join(names)}.',
              *advice,
              'To serve the learned policy for every task instead, start without --agent (--offline-only in Docker).')
        return False
    return True


class AgentRoute:
    def __init__(self, tasks, *, runtime_factory=None, preflight=None, camera_check=None):
        self.tasks = tasks
        self.runtime_factory = runtime_factory
        self.preflight = api_preflight if preflight is None else preflight
        self.camera_check = camera_problem if camera_check is None else camera_check
        self.entry = None
        self.epoch = None
        self.selected = None  # None (undecided) | 'base' | 'agent' | 'fallback'
        self.fallback_reason = None
        self.fallback_steps = 0
        self.runtime = None
        self.pending = None  # in-flight runtime.act call (an agent plan may span several steps)
        self.timeouts = 0
        self.answered = False
        # Own threads per connection: an agent query can block for minutes and must not
        # occupy the shared default executor or the base policy's JAX worker.
        self._pool = concurrent.futures.ThreadPoolExecutor(1, thread_name_prefix='agent-route')
        self._query_pool = concurrent.futures.ThreadPoolExecutor(1, thread_name_prefix='agent-query')

    async def call(self, fn, *args):
        import asyncio
        return await asyncio.get_running_loop().run_in_executor(self._pool, fn, *args)

    def reset(self, env_indices=None):
        self.close()
        self.epoch = uuid.uuid4().hex
        self.selected = None
        self.entry = None
        self.fallback_reason = None
        self.fallback_steps = 0
        self.timeouts = 0
        self.answered = False

    def step(self, obs):
        """Agent action for this observation, or None: the base policy handles it."""
        if self.selected == 'base':
            return None
        if self.selected == 'fallback':
            self.fallback_steps += 1
            if self.fallback_steps % FALLBACK_REMINDER_STEPS == 0:
                logging.error(f'{RED}AGENT FALLBACK ACTIVE ({self._task_name()}, {self.fallback_steps} steps on '
                              f'the learned policy): {self.fallback_reason}{RESET}')
            return None
        entry = self._routed_entry(obs)
        if self.selected == 'agent':
            if entry is not self.entry:
                self._fall_back('task changed without an evaluator reset')
                return None
            return self._act(obs)
        # First observation of the episode: warn about a wrong wrapper for every task.
        camera = self.camera_check(obs)
        if camera:
            alarm('WRONG OBSERVATIONS: ' + camera,
                  'Please run the evaluator with --env-wrapper omnigibson.eval.wrappers.RGBDFullResWrapper '
                  '(see agent/README.md).')
        if entry is None:
            self.selected = 'base'
            return None
        self.entry = entry
        problem = self._unsupported(obs) or camera
        if problem:
            self._fall_back(problem)
            return None
        self.selected = 'agent'
        return self._act(obs)

    def _routed_entry(self, obs):
        ids = np.asarray(obs.get('task_id', [])).reshape(-1)
        matched = [task for task in self.tasks if np.any(ids == task)]
        return self.tasks[matched[0]] if matched else None

    def _unsupported(self, obs):
        if self.epoch is None:
            return 'no evaluator reset on this connection (reconnect mid-episode?)'
        if (np.asarray(obs.get('task_id', [])).size != 1
                or np.asarray(obs[PROPRIO_KEY]).shape not in ((61,), (1, 61))):
            return 'the agent needs one environment per connection (--num-envs 1 or --policy-endpoints)'
        return None

    def _act(self, obs):
        start = time.monotonic()
        limit = QUERY_LIMIT_S if self.answered or self.timeouts else FIRST_QUERY_LIMIT_S
        try:
            if self.runtime is None:
                if os.environ.get('B1K_AGENT_PREFLIGHT', '1') == '1':
                    ok, message = self.preflight(agent_model(self.entry))
                    if not ok:
                        raise RuntimeError('OpenAI API check failed: ' + message)
                self.runtime = self._make_runtime()
            while True:
                if self.pending is None:
                    self.pending = self._query_pool.submit(self.runtime.act, obs)
                remaining = limit - (time.monotonic() - start)
                try:
                    action = self.pending.result(timeout=max(0.0, remaining))
                except TimeoutError as error:
                    # concurrent.futures.TimeoutError is the builtin since Python 3.11:
                    # a still-running call is our wait limit, a finished one raised itself.
                    if not self.pending.done():
                        return self._query_timeout(obs, limit)
                    if str(error) == BRIDGE_WAIT_TIMEOUT and not self._wall_budget_spent():
                        # The bridge's 599 s goal wait ended while the agent still plans:
                        # ask again with the newest observation (same controller tick).
                        self.pending = None
                        continue
                    raise
                self.pending = None
                break
            action = np.asarray(action).astype(np.float32)
            if action.shape != (1, 23) or not np.isfinite(action).all():
                raise ValueError(f'agent returned a bad action, shape {action.shape}')
        except Exception as error:
            self._fall_back(_mask(f'{type(error).__name__}: {error}'))
            return None
        self.timeouts = 0
        self.answered = True
        return action if np.ndim(obs[PROPRIO_KEY]) == 2 else action[0]

    def _query_timeout(self, obs, limit):
        self.timeouts += 1
        if self.timeouts >= MAX_QUERY_TIMEOUTS:
            self._fall_back(f'the agent did not answer within {MAX_QUERY_TIMEOUTS} consecutive '
                            f'query limits ({limit:.0f} s each)')
            return None
        logging.error(f'{RED}AGENT SLOW in {self._task_name()}: no answer within {limit:.0f} s '
                      f'({self.timeouts}/{MAX_QUERY_TIMEOUTS}); holding the robot still and waiting{RESET}')
        policy = getattr(self.runtime, 'policy', None)
        last = getattr(getattr(policy, 'controller', None), 'last_action', None)
        action = hold_action(obs, last)[None, :]
        return action if np.ndim(obs[PROPRIO_KEY]) == 2 else action[0]

    def _wall_budget_spent(self):
        policy = getattr(self.runtime, 'policy', None)
        started = getattr(policy, 'started', None)
        return started is not None and time.monotonic() - started >= policy.max_steps

    def _make_runtime(self):
        if self.runtime_factory is not None:
            return self.runtime_factory(self.epoch)
        # Only routed episodes import/start the agent runtime. Base-only episodes need no model auth
        # and no session files.
        if str(REPO) not in sys.path:
            sys.path.insert(0, str(REPO))
        from agent.eval.runtime import FrozenRuntime
        entry = dict(self.entry)
        entry['model'] = agent_model(self.entry)
        config = {
            'run_root': os.environ.get('B1K_AGENT_RUN_ROOT', '/tmp/behavior-agent/rollouts'),
            'pi_agent_dir': os.environ.get('PI_CODING_AGENT_DIR', '/tmp/behavior-agent/auth'),
            'query_limit_seconds': RUNTIME_QUERY_LIMIT_S,
            'continue_after_turn': True,
            'force_initial_turn_end': os.environ.get('B1K_AGENT_TEST_EARLY_TURN') == '1',
            'guard_extensions': [str(AGENT_ROOT / name) for name in GUARD_EXTENSIONS],
        }
        return FrozenRuntime(entry, self.epoch, config)

    def _task_name(self):
        return (self.entry or {}).get('task_name', '?')

    def _fall_back(self, reason):
        self.selected = 'fallback'
        self.fallback_reason = reason
        self.close()
        alarm(f'AGENT FAILED in {self._task_name()} (episode {self.epoch}): {reason}',
              'The rest of THIS episode runs with the learned policy; the next episode starts with the agent again.',
              'If this repeats, check the OpenAI key, quota and network.')

    def close(self):
        runtime, self.runtime = self.runtime, None
        self.pending = None
        if runtime is not None:
            try:
                runtime.close()
            except Exception as error:
                logging.error(f'{RED}agent runtime close failed: {_mask(error)}{RESET}')

    def shutdown(self):
        """Connection ended: stop the agent and release the route's threads."""
        self.close()
        self._query_pool.shutdown(wait=False, cancel_futures=True)
        self._pool.shutdown(wait=False, cancel_futures=True)
