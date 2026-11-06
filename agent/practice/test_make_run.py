"""CPU check of the practice run tooling: make_run.py + practice_client.py, with a fake READY worker."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def fake_worker(home, run, task, instance):
    runtime = home / 'runtime' / run
    (runtime / 'queue').mkdir(parents=True)
    manifest = runtime / 'manifest.json'
    manifest.write_text(json.dumps({'task_instance': {'task': task, 'native_instance_id': instance, 'scene': 'house',
                                                      'mode': 'train', 'official_nominal_step_budget': 7960}}))
    (runtime / 'queue/ready.json').write_text(json.dumps({'pid': 1, 'version': 'test', 'manifest': str(manifest)}))


def make_run(home, *args):
    return subprocess.run([sys.executable, str(HERE / 'bin/make_run.py'), *args], env={**os.environ, 'PRACTICE_HOME': str(home)},
                          check=True, capture_output=True, text=True).stdout


def main():
    with tempfile.TemporaryDirectory() as directory:
        home = Path(directory)
        fake_worker(home, 'trumpet-01', 'clean_a_trumpet', 20)
        assert 'RUN_READY' in make_run(home, 'clean_a_trumpet', '20', 'trumpet-01')
        campaign = home / 'campaign'; run = campaign / 'runs/trumpet-01'
        for name in ('PRACTICE-BRIEF.md', 'LESSONS.md', 'skill/behavior-sim-control/SKILL.md',
                     'task_pack/clean_a_trumpet/README.md', 'prior-practice/clean_a_trumpet/NOTES.md'):
            assert (campaign / name).is_file(), name
        setup = json.loads((run / 'SETUP.json').read_text())
        assert setup['exec_prefix'] == [] and setup['task_instance']['native_instance_id'] == 20
        kickoff = (run / 'PRACTICER-KICKOFF.md').read_text()
        assert '{{' not in kickoff and '7960 steps' in kickoff
        (campaign / 'LESSONS.md').write_text('appended lesson')
        fake_worker(home, 'trumpet-278', 'clean_a_trumpet', 278)
        assert 'zero_shot' in make_run(home, 'clean_a_trumpet', '278', 'trumpet-01', '--next', 'trumpet-278')
        assert (campaign / 'LESSONS.md').read_text() == 'appended lesson'   # never overwritten
        assert json.loads((run / 'SETUP.next.json').read_text())['zero_shot'] is True

        os.environ['BEHAVIOR_SIM_RUN_DIR'] = str(run)
        spec = importlib.util.spec_from_file_location('sim_client', run / 'sim_client.py')
        s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
        assert callable(s.admin_reset) and callable(s.observe)      # observe comes through practice_client
        assert (run / 'client_helpers/robot_kinematics.py').is_file()
        recipe = campaign / 'prior-practice/cook_brussels_sprouts/examples/study_sheets.py'
        help_run = subprocess.run([sys.executable, str(recipe), '--help'], capture_output=True, text=True)
        assert help_run.returncode == 0, help_run.stderr[-400:]      # archived recipes find their helpers
        sys.modules['sim_client'] = s
        namespace = {}
        exec('from sim_client import *', namespace)
        assert {'observe', 'act', 'xyz', 'admin_reset', 'snapshot'} <= set(namespace)
        # The CLI goes through the same holds and lock as Python calls.
        import fcntl
        lock = open(run / '.practice-call.lock', 'a')
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        held = subprocess.run([sys.executable, str(run / 'sim_client.py'), 'observe'], capture_output=True, text=True,
                              env={**os.environ, 'BEHAVIOR_SIM_RUN_DIR': str(run)})
        assert held.returncode != 0 and 'BlockingIOError' in held.stderr, held.stderr[-400:]
        lock.close()
        (run / 'ZERO-SHOT.json').write_text('{"instance": 278}')
        for name in ('snapshot', 'restore', 'practice_feedback'):
            try:
                getattr(s, name)('x') if name != 'practice_feedback' else s.practice_feedback()
            except RuntimeError as error:
                assert 'Zero-shot' in str(error)
            else:
                raise AssertionError(name + ' allowed during a zero-shot attempt')
        (run / 'STOP').write_text('user stop')
        try:
            s.observe('should be refused')
        except RuntimeError as error:
            assert 'Practice held' in str(error)
        else:
            raise AssertionError('STOP did not hold the client')
    print('MAKE_RUN_AND_PRACTICE_CLIENT_CPU_PASS')


if __name__ == '__main__':
    main()
