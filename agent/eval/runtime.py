"""One agent episode inside the policy server: a fresh Pi fork of a frozen practice session.

FrozenRuntime starts a loopback HTTP bridge (agent/control/official_policy_server.py), copies the task's
notes, examples and public task pack into a private run directory, and launches
`pi --fork <frozen session>` with the robot skill and the guard extensions. The evaluator's observations
drive the per-tick controller; the agent's observe/act calls set its goals. A normal turn end resumes the
same fork; any failure, deadline or guard stop ends the agent for this episode (the route then falls back
to the learned policy). There is no scene reset, no retry and no action replay.
"""
import hashlib
import importlib
import json
import os
import secrets
from pathlib import Path
import signal
import subprocess
import sys
import sysconfig
import threading
import time
from http.server import ThreadingHTTPServer

from .frozen import AGENT_ROOT, copy_checked, member, sha256, support_source

CONTROL = AGENT_ROOT / 'control'
PI = AGENT_ROOT / 'pi'
EVAL_BRIEF = Path(__file__).resolve().parent / 'EVAL-BRIEF.md'
SKILL = PI / 'skills/behavior-sim-control/SKILL.md'
OBSERVATION_EXTENSION = PI / 'extensions/observation_delivery.ts'
REPLAY_EXTENSION = PI / 'extensions/replay.ts'


def verified_assets(entry, task_root):
    """Frozen session plus its notes/examples/pack, all checked against the hashes in tasks.json."""
    task = entry['task_name']
    snapshot = member(Path(task_root), task + '/session.jsonl')
    if not snapshot.is_file():
        raise FileNotFoundError(f'No frozen session for {task}; run python -m agent.eval.frozen')
    if sha256(snapshot) != entry['session']['sha256']:
        raise ValueError('Frozen session hash mismatch')
    for name, expected in entry['support'].items():
        if sha256(support_source(Path(task_root), task, name)) != expected:
            raise ValueError('Frozen support hash mismatch: ' + name)
    return snapshot


def controller_adapter(profile, max_steps, epoch):
    """Per-tick controller policy + HTTP bridge from agent/control (no process or socket yet)."""
    # Refuse a same-named module already imported from another copy of the controller.
    for path in CONTROL.glob('*.py'):
        module = sys.modules.get(path.stem)
        if module and Path(getattr(module, '__file__', '')).resolve() != path.resolve():
            raise RuntimeError('Conflicting imported module: ' + path.stem)
    if str(CONTROL) not in sys.path:
        sys.path.insert(0, str(CONTROL))
    server = importlib.import_module('official_policy_server')
    controller = importlib.import_module('official_controller')
    bridge = server.AgentBridge()
    policy = controller.OfficialControllerPolicy(profile, bridge, max_steps)
    bridge.policy = policy
    bridge.epoch = epoch
    return policy, bridge


def successful_json_turn(path, offset=0):
    """JSON mode may exit0 on failure. Inspect only final outcome metadata."""
    reason = None
    settled = False
    try:
        with Path(path).open('rb') as stream:
            stream.seek(offset)
            for line in stream:
                if not line.endswith(b'\n'):
                    return False
                event = json.loads(line)
                if event.get('type') == 'agent_start':
                    reason, settled = None, False
                elif event.get('type') == 'message_end' and event.get('message', {}).get('role') == 'assistant':
                    reason = event['message'].get('stopReason')
                    settled = False
                elif event.get('type') == 'agent_settled':
                    settled = event.get('aborted') is False
        return settled and reason == 'stop'
    except (OSError, ValueError, TypeError):
        return False


class FrozenRuntime:
    def __init__(self, entry, epoch, config, *, actor_command=None):
        # actor_command is a CPU-test injection seam, never configurable via JSON/CLI.
        if len(epoch) != 32 or any(c not in '0123456789abcdef' for c in epoch):
            raise ValueError('Invalid rollout epoch')
        self.child = None
        self.http = None
        self.bridge = None
        self.stop_event = threading.Event()
        self.child_stop_lock = threading.Lock()
        self.query_started = None
        self.resume_count = 0
        self.resumes = []
        self.event_offset = 0
        self.actor_command = actor_command
        self.continue_after_turn = config.get('continue_after_turn', True)
        self.qualification_only = bool(config.get('qualification_only'))
        self.started = time.monotonic()  # Includes hashing, fork startup and all later waits.
        self.max_steps = int(entry['max_steps'])
        self.query_limit = float(config.get('query_limit_seconds', 570))
        if self.max_steps < 1 or not 0 < self.query_limit <= 660:
            raise ValueError('Finite horizon/query limit required')
        self.run = Path(config['run_root']).resolve() / epoch
        self.run.mkdir(parents=True, exist_ok=False, mode=0o700)
        self.replay = None
        if os.environ.get('B1K_AGENT_REPLAY') == '1':
            from .replay_recording import ReplayRecorder
            self.replay = ReplayRecorder(self.run, epoch)
            self.replay.emit('episode_start', task=entry['task_name'], model=entry['model'],
                             thinking=entry['thinking'], frozen_session_sha256=entry['session']['sha256'])
        try:
            # Provider retries cover HTTP failures; one same-session recovery
            # also covers transient response.failed events after a stream opens.
            # Pi omits the failed assistant response, preserving completed tools.
            # Both layers remain inside the existing query/episode watchdogs.
            # A randomized base jitters the single outer retry across workers.
            retry_settings = {'retry': {'enabled': True, 'maxRetries': 1,
                'baseDelayMs': 2000 + secrets.randbelow(2001), 'maxAgentDelayMs': 60000,
                'provider': {'maxRetries': 3, 'maxRetryDelayMs': 0}}}
            # No provider delay cap: honor Retry-After until the query watchdog
            # cancels, instead of retrying early after a delay-cap exception.
            pi_settings = self.run / '.pi' / 'settings.json'
            pi_settings.parent.mkdir(mode=0o700)
            pi_settings.write_text(json.dumps(retry_settings, indent=2) + '\n')
            task_root = Path(config.get('task_root', AGENT_ROOT / 'tasks'))
            snapshot = verified_assets(entry, task_root)
            for name, expected in entry['support'].items():
                copy_checked(support_source(task_root, entry['task_name'], name), member(self.run, name), expected)
            profile = json.loads((CONTROL / 'static-profile.json').read_text())
            self.policy, self.bridge = controller_adapter(profile, self.max_steps, epoch)
            self.policy.started = self.started
            from official_policy_server import handler_for
            original_rpc = self.bridge.rpc
            self.public_calls = []
            def recorded_rpc(job):
                result = self.replay.rpc(original_rpc, job) if self.replay else original_rpc(job)
                self.public_calls.append({'op': job['op'], 'request_id': job['request_id'],
                    'observation_id': result.get('observation_id'),
                    'executed_ticks': result.get('execution', {}).get('executed_ticks'),
                    'ended': result.get('ended', False)})
                (self.run / 'PUBLIC-CALLS.json').write_text(json.dumps(self.public_calls, indent=2) + '\n')
                return result
            self.bridge.rpc = recorded_rpc
            runtime = self
            parent = handler_for(self.bridge)
            class Handler(parent):
                def do_POST(self):
                    if self.path == '/finish' and runtime.continue_after_turn and not runtime.qualification_only:
                        # A planner cannot terminate the official episode or latch hold-only mode.
                        size = int(self.headers.get('Content-Length', 0))
                        if self.headers.get('X-Behavior-Rollout') != epoch or not 0 < size < 40000:
                            self.send_error(403, 'Wrong epoch or invalid finish request'); return
                        self.rfile.read(size)
                        raw = b'{"finished":false,"episode_still_running":true,"instruction":"Continue until evaluator termination"}'
                        self.send_response(200); self.send_header('Content-Type', 'application/json')
                        self.send_header('Content-Length', str(len(raw))); self.end_headers(); self.wfile.write(raw)
                        return
                    # No actor-controlled final observations or arbitrary /end injection.
                    if self.path == '/end':
                        self.send_error(403, 'Only evaluator reset/close ends this binding')
                        return
                    super().do_POST()
                    if self.path == '/finish' and runtime.bridge.finished:
                        (runtime.run / 'FINISHED.json').write_text(json.dumps({
                            'epoch': epoch, 'public_calls': runtime.public_calls,
                            'completed_goals': len(runtime.policy.completed_goals),
                            'resume_count': runtime.resume_count,
                            'qualification_only': bool(config.get('qualification_only')),
                        }, indent=2) + '\n')
            self.http = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
            self.http.daemon_threads = True
            threading.Thread(target=self.http.serve_forever, daemon=True).start()
            url = f'http://127.0.0.1:{self.http.server_port}'
            # The agent imports this copy; its kinematics helpers stay in agent/control.
            source_client = CONTROL / 'sim_client.py'
            copy_checked(source_client, self.run / 'sim_client.py', sha256(source_client))
            # Practised recipes in examples/ import helpers from <run>/client_helpers.
            (self.run / 'client_helpers').symlink_to(CONTROL, target_is_directory=True)
            setup = dict(status='READY', transport='official_http', evaluation_url=url, protocol=6,
                         task=entry['task_name'], epoch=epoch, max_steps=self.max_steps,
                         wall_budget_seconds=self.max_steps, client_helpers=str(CONTROL))
            (self.run / 'SETUP.json').write_text(json.dumps(setup, indent=2) + '\n')
            (self.run / 'sitecustomize.py').write_text(
                "import importlib.abc, importlib.util, os, sys\n"
                "sys.path.insert(0, os.environ['BEHAVIOR_PYTHON_SITE'])\n"
                "class EvaluationClient(importlib.abc.MetaPathFinder):\n"
                " def find_spec(self,fullname,path=None,target=None):\n"
                "  if fullname=='sim_client': return importlib.util.spec_from_file_location(fullname,os.environ['BEHAVIOR_EVAL_RUN_DIR']+'/sim_client.py')\n"
                "sys.meta_path.insert(0,EvaluationClient())\n")
            brief = EVAL_BRIEF.read_text()
            for key, value in {'TASK': entry['task_name'], 'RUN_DIR': str(self.run),
                               'MAX_STEPS': str(self.max_steps)}.items():
                brief = brief.replace('{{' + key + '}}', value)
            if config.get('force_initial_turn_end'):
                brief += ('\n## Continuation verification\n'
                    'After reading NOTES.md, deliberately end this first turn once before observe/act. '
                    'When the runner resumes this same session, continue the full official task normally. '
                    'This adds no time or attempts and does not change the task or native termination.\n')
            if config.get('qualification_only'):
                brief += ('\n## Qualification-only override\n'
                    'This is an integration smoke, NOT a full-task attempt. First read task_pack/' + entry['task_name'] + '/README.md, then NOTES.md and '
                    'END THIS FIRST TURN once without observe/act, to test automatic same-session continuation. '
                    'When the one-line continuation prompt arrives, call s.observe(), inspect the delivered RGB/state, then call exactly one '
                    's.act(intent="First official integration action", left={"grip": 1.0}, '
                    'right={"grip": 1.0}, max_steps=1, accept_partial=True). '
                    'Do not navigate or attempt the task. Inspect its returned RGB/state; '
                    'call s.admin_finish("qualification-first-observe-act") and stop.\n')
            (self.run / 'EVAL-BRIEF.md').write_text(brief)
            env = {k: v for k, v in os.environ.items() if not k.startswith(('TMUX', 'CMUX', 'PI_SESSION'))}
            env.update(BEHAVIOR_EVAL_RUN_DIR=str(self.run), BEHAVIOR_SIM_RUN_DIR=str(self.run),
                       BEHAVIOR_EVAL_URL=url,
                       BEHAVIOR_PYTHON_SITE=sysconfig.get_paths()['purelib'], PYTHONPATH=str(self.run),
                       PI_CODING_AGENT_DIR=str(Path(config['pi_agent_dir']).resolve()),
                       OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
            if actor_command is None:
                guards = config.get('guard_extensions', [])
                if not guards:
                    raise ValueError('Cost/auth guard extensions are required')
                command = ['pi', '--fork', str(snapshot), '--session-dir', str(self.run / 'sessions'),
                    '--session-id', 'eval-' + epoch, '--model', entry['model'], '--thinking', entry['thinking'],
                    # Trust only this freshly created, hash-audited rollout directory
                    # so Pi loads its retry settings; automatic discovery stays disabled.
                    '--mode', 'json', '--approve', '--no-context-files', '--no-skills', '--no-prompt-templates',
                    '--no-extensions', '--no-mcp', '-e', 'builtin:codemode', '-e', str(OBSERVATION_EXTENSION),
                    '--skill', str(SKILL)]
                for guard in guards:
                    command.extend(['-e', str(Path(guard).resolve())])
                if self.replay:
                    command.extend(['-e', str(REPLAY_EXTENSION)])
                command.extend(['--tools', 'read,bash,edit,write,codemode',
                    'Read EVAL-BRIEF.md, then task_pack/' + entry['task_name'] + '/README.md FIRST, then NOTES.md. Observe before acting.'])
            else:
                command = list(actor_command)
            # Provenance of this episode: which frozen context, runtime, skill and guards it ran with.
            (self.run / 'FORK.json').write_text(json.dumps({
                'epoch': epoch, 'session_sha256': entry['session']['sha256'],
                'model': entry['model'], 'thinking': entry['thinking'], 'test_actor': actor_command is not None,
                'runtime_sha256': sha256(Path(__file__)),
                'entry_sha256': hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest(),
                'skill_sha256': sha256(SKILL),
                'initial_files_sha256': {str(p.relative_to(self.run)): sha256(p)
                    for p in self.run.rglob('*') if p.is_file() and not p.is_symlink()},
                'guard_extensions': {Path(g).name: sha256(g) for g in config.get('guard_extensions', [])},
                'replay_recording': bool(self.replay),
            }, indent=2) + '\n')
            self.command = command
            self.env = env
            with (self.run / 'events.jsonl').open('xb') as stdout, (self.run / 'stderr.log').open('xb') as stderr:
                self.child = subprocess.Popen(command, cwd=self.run, env=env,
                    stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr, start_new_session=True)
            print('FROZEN_FORK_STARTED', epoch, self.child.pid, flush=True)
            self.watchdog = threading.Thread(target=self._watch, daemon=True)
            self.watchdog.start()
        except BaseException:
            self.close()
            raise

    def _fail(self, reason):
        if self.bridge:
            with self.bridge.cv:
                self.bridge.error = reason
                self.bridge.cv.notify_all()

    def _watch(self):
        while not self.stop_event.wait(.05):
            now = time.monotonic()
            if now - self.started >= self.max_steps:
                self._fail('Episode wall deadline')
                self._stop_child()
                return
            if self.query_started is not None and now - self.query_started >= self.query_limit:
                self._fail('Query deadline (transport reserve retained)')
                self._stop_child()
                return
            code = self.child.poll()
            if code is not None:
                if self.qualification_only and self.bridge.finished:
                    return  # The evaluator test runner ends this deliberately bounded smoke.
                # Normal turn completion is resumable; process/provider/safety failures
                # are not permission to retry or bypass a guard.
                if code == 0 and self.continue_after_turn and not self.bridge.error and not self.bridge.ended:
                    if self.actor_command is None and not successful_json_turn(self.run/'events.jsonl', self.event_offset):
                        self._fail('Actor did not settle with a successful assistant turn; refusing continuation')
                        return
                    try:
                        self._resume(code)
                    except Exception as error:
                        self._fail('Same-session continuation failed: ' + str(error))
                        return
                    continue
                if code != 0 or not self.bridge.finished:
                    self._fail('Actor exited without explicit finish; exit=' + str(code))
                return

    def _resume(self, exit_code):
        # No new fork, reset, clock, controller, observation cache or action replay.
        # Short event-driven backoff prevents a fast failing CLI from busy-spinning.
        if self.stop_event.wait(.25):
            return
        with self.child_stop_lock:
            if self.stop_event.is_set() or self.bridge.error or self.bridge.ended:
                return
            session_file = None
            if self.actor_command is not None:
                command = list(self.actor_command)  # CPU-only lifecycle test seam.
            else:
                sessions = list((self.run / 'sessions').glob('*.jsonl'))
                if len(sessions) != 1:
                    raise RuntimeError('Expected exactly one persisted rollout fork; refusing a new session')
                session_file = sessions[0]
                with session_file.open() as stream:
                    header = json.loads(stream.readline())
                if header.get('id') != 'eval-' + self.bridge.epoch:
                    raise RuntimeError('Persisted fork identity changed')
                command = [self.command[0], '--session', str(session_file)]
                i = 1
                while i < len(self.command)-1:
                    if self.command[i] in ('--fork', '--session-id'):
                        i += 2
                    else:
                        command.append(self.command[i]); i += 1
                command.append('Episode still running: continue; never stop before the evaluator ends the episode.')
            # Never reset bridge/controller state. /finish is nonterminal in full rollouts.
            self.resume_count += 1
            self.resumes.append({'continuation': self.resume_count, 'previous_exit_code': exit_code,
                'session_file': str(session_file) if session_file else None,
                'epoch': self.bridge.epoch, 'native_tick': self.policy.tick,
                'elapsed_seconds': time.monotonic()-self.started, 'test_actor': self.actor_command is not None})
            (self.run / 'RESUMES.json').write_text(json.dumps(self.resumes, indent=2) + '\n')
            self.event_offset = (self.run / 'events.jsonl').stat().st_size
            with (self.run / 'events.jsonl').open('ab') as stdout, (self.run / 'stderr.log').open('ab') as stderr:
                self.child = subprocess.Popen(command, cwd=self.run, env=self.env,
                    stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr, start_new_session=True)
            print('SAME_FORK_CONTINUED', self.bridge.epoch, self.resume_count, self.child.pid, exit_code, flush=True)

    def act(self, flat):
        self.query_started = time.monotonic()
        try:
            if self.bridge.error:
                raise RuntimeError(self.bridge.error)
            if self.stop_event.is_set():
                raise RuntimeError('Closed rollout')
            if self.policy.goal and self.policy.goal['id'] in self.bridge.cancelled:
                self.policy.controller.reason = 'cancelled'
            return self.policy.act(flat)
        finally:
            self.query_started = None

    def _stop_child(self):
        # Watchdog and reset/close can arrive together; never signal a reaped PGID.
        with self.child_stop_lock:
            child = self.child
            if child and child.poll() is None:
                try:
                    os.killpg(child.pid, signal.SIGTERM)
                    child.wait(timeout=3)
                except ProcessLookupError:
                    pass
                except subprocess.TimeoutExpired:
                    try:
                        os.killpg(child.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    child.wait(timeout=3)

    def close(self):
        self.stop_event.set()
        self._fail('Rollout closed/reset; terminal action acknowledgement unknown')
        self._stop_child()
        if self.http:
            self.http.shutdown()
            self.http.server_close()
            self.http = None
        if self.bridge:
            (self.run / 'CLOSED.json').write_text(json.dumps({
                'epoch': self.bridge.epoch, 'native_actions_emitted': self.policy.tick,
                'last_action_execution_confirmed': False, 'error': self.bridge.error,
                'actor_exit_code': self.child.poll() if self.child else None,
            }, indent=2) + '\n')


def factory(config):
    return lambda entry, epoch: FrozenRuntime(entry, epoch, config)
