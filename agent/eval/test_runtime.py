"""Offline checks only: synthetic official observations, real local HTTP, no model/GPU.

Run from the repository root: python -m unittest agent.eval.test_runtime
"""
import copy
import gzip
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
import uuid

import numpy as np

from . import frozen, package, runtime
from .frozen import AGENT_ROOT, sha256

sys.path.insert(0, str(AGENT_ROOT / 'control'))
from test_portable_control import RobotModel, robot_fixture, advance  # noqa: E402
from test_official_controller import encode  # noqa: E402


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(frozen.REGISTRY.read_text())

    def test_registry_support_files_in_git_match_their_hashes(self):
        for task, entry in self.registry['tasks'].items():
            self.assertIn('NOTES.md', entry['support'])
            for name, digest in entry['support'].items():
                if name in entry['bundle']:
                    continue
                self.assertEqual(sha256(frozen.support_source(frozen.REGISTRY.parent, task, name)), digest, name)

    def test_build_without_bundle_disables_tasks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); tasks = root / 'tasks'; tasks.mkdir()
            registry = tasks / 'tasks.json'
            registry.write_text(json.dumps({'schema': 2, 'tasks': {'demo_task': {
                'task_id': 7, 'enabled': True, 'max_steps': 10, 'support': {'NOTES.md': '0' * 64}, 'bundle': [],
                'session': {'sha256': '0' * 64, 'bytes': 1, 'parts': [{'name': 'demo_task-00.jsonl.gz', 'bytes': 1,
                                                                        'sha256': '0' * 64}]}}}}))
            with self.assertRaises(FileNotFoundError):
                frozen.materialize(registry, root / 'frozen')
            frozen.materialize(registry, root / 'frozen', disable_missing=True)
            self.assertFalse(json.loads(registry.read_text())['tasks']['demo_task']['enabled'])

    def test_support_names_cannot_escape(self):
        for name in ('../x', '/etc/passwd', 'task_pack/other_task/README.md', 'session.jsonl'):
            with self.assertRaises(ValueError):
                frozen.support_source('/tmp', 'hanging_pictures', name)

    def test_package_then_materialize_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); tasks = root / 'tasks'; tasks.mkdir(); parts = root / 'frozen'
            registry = tasks / 'tasks.json'; registry.write_text('{"schema": 2, "tasks": {}}')
            run = root / 'run'; (run / 'examples').mkdir(parents=True); pack = root / 'pack'; pack.mkdir()
            (run / 'NOTES.md').write_text('synthetic note')
            (run / 'examples/grasp.md').write_text('synthetic recipe')
            (run / 'examples/big.json').write_text('[' + '0,' * 60000 + '0]')
            (pack / 'README.md').write_text('synthetic pack')
            session = root / 'session.jsonl'
            session.write_text(''.join(json.dumps({'type': 'message', 'i': i}) + '\n' for i in range(5)))
            key = b'sk-test-' + b'k' * 40
            package.package('demo_task', 7, 100, session, run, pack, key, registry, parts)
            entry = json.loads(registry.read_text())['tasks']['demo_task']
            self.assertFalse(entry['enabled'])
            self.assertEqual(entry['bundle'], ['examples/big.json'])
            self.assertEqual(sorted(entry['support']), ['NOTES.md', 'examples/big.json', 'examples/grasp.md',
                                                        'task_pack/demo_task/README.md'])
            self.assertTrue((tasks / 'demo_task/pack/README.md').is_file())
            frozen.restore_support('demo_task', entry, parts, tasks)
            self.assertEqual(frozen.materialize_task('demo_task', entry['session'], parts, tasks), 'assembled')
            self.assertEqual(sha256(tasks / 'demo_task/session.jsonl'), sha256(session))
            self.assertEqual(frozen.materialize_task('demo_task', entry['session'], parts, tasks), 'verified')
            with self.assertRaises(ValueError):  # already packaged
                package.package('demo_task', 7, 100, session, run, pack, key, registry, parts)
            leaked = root / 'leaked.jsonl'; leaked.write_text(json.dumps({'text': key.decode()}) + '\n')
            other = json.loads(registry.read_text()); other['tasks'].pop('demo_task'); registry.write_text(json.dumps(other))
            with self.assertRaises(ValueError):
                package.package('leak_task', 8, 100, leaked, run, pack, key, registry, parts)
            # A corrupted part is refused.
            part = parts / entry['session']['parts'][0]['name']
            with gzip.open(part, 'wb') as stream:
                stream.write(b'corrupt')
            (tasks / 'demo_task/session.jsonl').unlink()
            with self.assertRaises(ValueError):
                frozen.materialize_task('demo_task', entry['session'], parts, tasks)

    def fixture(self, root):
        """Tiny trusted assets, not an actual practice session or model call."""
        tasks = root / 'tasks'; task = tasks / 'hanging_pictures'; task.mkdir(parents=True)
        (task / 'session.jsonl').write_text('{"type":"session","version":3,"id":"cpu-only"}\n')
        (task / 'NOTES.md').write_text('CPU fixture; no task-solving evidence.')
        entry = copy.deepcopy(self.registry['tasks']['hanging_pictures'])
        entry.update(self.registry['defaults'], task_name='hanging_pictures', max_steps=30, bundle=[],
                     support={'NOTES.md': sha256(task / 'NOTES.md')})
        entry['session']['sha256'] = sha256(task / 'session.jsonl')
        config = {'task_root': str(tasks), 'run_root': str(root / 'runs'), 'pi_agent_dir': str(root / 'unused-auth'),
                  'query_limit_seconds': 5, 'continue_after_turn': False}
        return entry, config

    def test_asset_hash_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            entry, config = self.fixture(Path(d))
            entry['session']['sha256'] = '0' * 64
            with self.assertRaises(ValueError):
                runtime.verified_assets(entry, config['task_root'])
            entry, config = self.fixture(Path(d) / 'second')
            (Path(config['task_root']) / 'hanging_pictures/NOTES.md').write_text('changed')
            with self.assertRaises(ValueError):
                runtime.verified_assets(entry, config['task_root'])

    def test_real_http_client_and_controller(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);entry,config=self.fixture(root)
            config.update(continue_after_turn=True,qualification_only=True)
            actor=root/'actor.py';actor.write_text('''import json
from pathlib import Path
# End the initial turn before any action; the runtime must resume without reset.
if not Path('EARLY-TURN.txt').exists():
    Path('EARLY-TURN.txt').write_text('ended once')
    raise SystemExit(0)
import sim_client as s
obs=s.observe('CPU official observation')
q=list(obs['robot']['left']['joints']);q[3]-=.06
result=s.act('CPU capped goal',left={'q':q,'grip':1},right={'grip':1},max_steps=3)
assert result['execution']['executed_ticks']==3
assert s.xyz('head').shape==(720,720,3)
try:s.admin_reset()
except RuntimeError:pass
else:raise AssertionError('reset exposed')
Path('CPU_ACTOR_RESULT.json').write_text(json.dumps({'ticks':result['execution']['executed_ticks'],'xyz':True}))
s.admin_finish('cpu-complete')
''')
            instance=runtime.FrozenRuntime(entry,uuid.uuid4().hex,config,actor_command=[sys.executable,str(actor)])
            try:
                model=RobotModel();r=robot_fixture(model);profile=instance.policy.profile
                for tick in range(30):
                    obs=encode(r);obs['task_id']=np.array([[34]],dtype=np.int64)
                    for camera,meta in profile['cameras'].items():
                        h,w=meta['image_size_hw'];prefix=meta['observation_prefix']
                        obs[prefix+'::rgb']=np.full((1,h,w,4),tick,dtype=np.uint8)
                        obs[prefix+'::depth_linear']=np.ones((1,h,w),dtype=np.float32)
                    action=instance.act(obs)
                    self.assertEqual(action.shape,(1,23));advance(r,action[0],model)
                    if instance.bridge.finished:break
                self.assertTrue(instance.bridge.finished)
                self.assertEqual(instance.resume_count,1)
                self.assertEqual(instance.policy.reset_count,1)
                self.assertEqual(len(instance.policy.completed_goals),1)
                self.assertNotIn('untrusted_object_pose',instance.policy.packet)
                self.assertIsNone(instance.policy.packet['robot']['left']['joint_efforts_nm'])
                instance.child.wait(timeout=5);self.assertEqual(instance.child.returncode,0)
                self.assertTrue(json.loads((instance.run/'CPU_ACTOR_RESULT.json').read_text())['xyz'])
                url=f'http://127.0.0.1:{instance.http.server_port}'
                request=urllib.request.Request(url+'/rpc',data=b'{}',headers={'X-Behavior-Rollout':'stale'})
                with urllib.request.urlopen(request) as response:self.assertIn('stale',json.load(response)['error'])
                with self.assertRaises(urllib.error.HTTPError):
                    urllib.request.urlopen(urllib.request.Request(url+'/end',data=b'{}'))
            finally:instance.close()
            self.assertIsNotNone(instance.child.poll())

    def test_json_completion_not_exit_code_controls_continuation(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'events.jsonl'
            def outcome(reason,aborted=False,settled=True):
                rows=[{'type':'agent_start'}, {'type':'message_end','message':{'role':'assistant','stopReason':reason}}]
                if settled:rows.append({'type':'agent_settled','aborted':aborted})
                return ''.join(json.dumps(x)+'\n' for x in rows)
            for reason,abort,settled,expected in [('stop',False,True,True),('error',False,True,False),
                    ('aborted',True,True,False),('stop',True,True,False),('stop',False,False,False),
                    ('length',False,True,False),('toolUse',False,True,False)]:
                path.write_text(outcome(reason,abort,settled))
                self.assertEqual(runtime.successful_json_turn(path),expected)
            previous=outcome('stop');path.write_text(previous+'{"type":"agent_start"}\n')
            self.assertFalse(runtime.successful_json_turn(path,len(previous.encode())))
            path.write_text(previous+'{');self.assertFalse(runtime.successful_json_turn(path))

    def test_provider_retry_settings_are_scoped_and_audited(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); entry, config = self.fixture(root)
            auth = Path(config['pi_agent_dir']); auth.mkdir()
            global_settings = auth / 'settings.json'
            original = '{"retry":{"enabled":true,"provider":{"maxRetries":99}}}\n'
            global_settings.write_text(original)
            instance = runtime.FrozenRuntime(entry, uuid.uuid4().hex, config,
                actor_command=[sys.executable, '-c', 'import time; time.sleep(30)'])
            try:
                settings = instance.run / '.pi/settings.json'
                retry = json.loads(settings.read_text())['retry']
                self.assertTrue(retry['enabled'])
                self.assertEqual(retry['maxRetries'], 1)
                self.assertGreaterEqual(retry['baseDelayMs'], 2000)
                self.assertLessEqual(retry['baseDelayMs'], 4000)
                self.assertEqual(retry['provider'], {'maxRetries': 3, 'maxRetryDelayMs': 0})
                self.assertEqual(global_settings.read_text(), original)
                fork = json.loads((instance.run / 'FORK.json').read_text())
                self.assertEqual(fork['initial_files_sha256']['.pi/settings.json'], sha256(settings))
                self.assertEqual(instance.resume_count, 0)
            finally:
                instance.close()

    def test_nonzero_actor_failure_is_not_retried(self):
        with tempfile.TemporaryDirectory() as d:
            entry,config=self.fixture(Path(d));config['continue_after_turn']=True
            instance=runtime.FrozenRuntime(entry,uuid.uuid4().hex,config,
                actor_command=[sys.executable,'-c','raise SystemExit(3)'])
            try:
                with instance.bridge.cv:
                    self.assertTrue(instance.bridge.cv.wait_for(lambda:bool(instance.bridge.error),timeout=3))
                self.assertEqual(instance.resume_count,0)
                self.assertIn('exit=3',instance.bridge.error)
            finally:instance.close()

    def test_pending_query_timeout_and_close(self):
        for timeout in (False, True):
            with tempfile.TemporaryDirectory() as d:
                root=Path(d);entry,config=self.fixture(root)
                if timeout:config['query_limit_seconds']=.15
                else:config['continue_after_turn']=True
                instance=runtime.FrozenRuntime(entry,uuid.uuid4().hex,config,
                    actor_command=[sys.executable,'-c','import time; time.sleep(30)'])
                errors=[]
                # Sufficient native official shape for the initial goal wait.
                model=RobotModel();obs=encode(robot_fixture(model))
                for meta in instance.policy.profile['cameras'].values():
                    h,w=meta['image_size_hw'];prefix=meta['observation_prefix']
                    obs[prefix+'::rgb']=np.zeros((1,h,w,3),dtype=np.uint8)
                    obs[prefix+'::depth_linear']=np.ones((1,h,w),dtype=np.float32)
                def query():
                    try:instance.act(obs)
                    except Exception as error:errors.append(str(error))
                worker=threading.Thread(target=query);worker.start()
                with instance.bridge.cv:
                    instance.bridge.cv.wait_for(lambda:instance.bridge.waiting,timeout=3)
                if not timeout:
                    request=urllib.request.Request(f'http://127.0.0.1:{instance.http.server_port}/finish',
                        data=b'{}',headers={'X-Behavior-Rollout':instance.bridge.epoch})
                    with urllib.request.urlopen(request) as response:self.assertFalse(json.load(response)['finished'])
                    self.assertFalse(instance.bridge.finished)
                    instance.close()
                worker.join(5);instance.close()
                self.assertFalse(worker.is_alive());self.assertTrue(errors)
                self.assertIsNotNone(instance.child.poll())


if __name__=='__main__':unittest.main(verbosity=2)
