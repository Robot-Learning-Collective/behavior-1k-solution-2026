#!/usr/bin/env python3
"""Create a practice run bound to a READY worker (bin/worker.sh), or stage a new layout for an existing run.

    agent/practice/bin/make_run.py TASK INSTANCE RUN               new run, e.g. clean_a_trumpet 20 trumpet-01
    agent/practice/bin/make_run.py TASK INSTANCE RUN --next WORKER  stage worker run WORKER (a new instance) as
                                                                    RUN's SETUP.next.json; zero-shot by default

The campaign (<PRACTICE_HOME>/campaign, default <repo>/.practice) holds what every practicer reads: the brief,
the cross-task lessons, the skill, public task packs and earlier practicers' notes. Each run directory holds
SETUP.json, a sim_client.py that routes through agent/practice/practice_client.py, the kickoff, NOTES.md and
examples/. The agent's own next admin_reset switches a run to a staged layout.
"""
import argparse
import json
import os
from pathlib import Path
import shutil

AGENT = Path(__file__).resolve().parents[2]
PRACTICE = AGENT / 'practice'
HOME = Path(os.environ.get('PRACTICE_HOME', AGENT.parent / '.practice'))
CAMPAIGN = HOME / 'campaign'
CLIENT = '''"""Practice client for this run: agent/practice/practice_client.py over agent/control/sim_client.py."""
import sys
sys.path.insert(0, {practice!r})
from practice_client import *  # noqa: F401,F403
from practice_client import __getattr__, main  # noqa: F401

if __name__ == '__main__':
    main()
'''


def campaign():
    """Shared, idempotent. LESSONS.md is never overwritten: practicers append to it."""
    for name in ('runs', 'task_pack', 'prior-practice'):
        (CAMPAIGN / name).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PRACTICE / 'prompts/PRACTICE-BRIEF.md', CAMPAIGN / 'PRACTICE-BRIEF.md')
    if not (CAMPAIGN / 'LESSONS.md').exists():
        shutil.copyfile(PRACTICE / 'prompts/LESSONS.md', CAMPAIGN / 'LESSONS.md')
    shutil.copytree(PRACTICE / 'skill', CAMPAIGN / 'skill', dirs_exist_ok=True)
    for task in sorted(p for p in (AGENT / 'tasks').iterdir() if p.is_dir()):
        if (task / 'pack').is_dir():
            shutil.copytree(task / 'pack', CAMPAIGN / 'task_pack' / task.name, dirs_exist_ok=True)
        prior = CAMPAIGN / 'prior-practice' / task.name
        if not prior.exists():
            prior.mkdir()
            shutil.copyfile(task / 'NOTES.md', prior / 'NOTES.md')
            if (task / 'examples').is_dir():
                shutil.copytree(task / 'examples', prior / 'examples')
        if not (prior / 'client_helpers').exists():
            (prior / 'client_helpers').symlink_to(AGENT / 'control', target_is_directory=True)


def binding(task, instance, worker_run):
    runtime = HOME / 'runtime' / worker_run
    ready = json.loads((runtime / 'queue/ready.json').read_text())
    task_instance = json.loads(Path(ready['manifest']).read_text())['task_instance']
    if (task_instance['task'], task_instance['native_instance_id']) != (task, instance):
        raise SystemExit(f'Worker {worker_run} runs {task_instance["task"]} instance {task_instance["native_instance_id"]}')
    return {
        'status': 'READY', 'protocol': 6, 'practice': True, 'snapshot_restore': True, 'practice_feedback': True,
        'queue': str(runtime / 'queue'), 'exec_prefix': [],
        'remote_rpc': str(PRACTICE / 'rpc.py'), 'remote_admin': str(PRACTICE / 'admin.py'),
        'rpc_transport': {'version': 'framed-policy-v1', 'remote_rpc': str(PRACTICE / 'rpc.py')},
        'client_helpers': str(AGENT / 'control'), 'local_observation_root': str(HOME / 'obs'),
        'observation_namespace': f'{worker_run}_obs', 'worker_pid': ready['pid'], 'behavior_version': ready['version'],
        'task_instance': task_instance,
    }


def new_run(task, instance, name):
    run = CAMPAIGN / 'runs' / name
    run.mkdir(parents=True, exist_ok=False)
    (run / 'examples').mkdir()
    setup = binding(task, instance, name)
    (run / 'SETUP.json').write_text(json.dumps(setup, indent=2) + '\n')
    (run / 'sim_client.py').write_text(CLIENT.format(practice=str(PRACTICE)))
    (run / 'client_helpers').symlink_to(AGENT / 'control', target_is_directory=True)  # path older recipes import
    kickoff = (PRACTICE / 'prompts/PRACTICER-KICKOFF.md').read_text()
    for key, value in {'TASK': task, 'INSTANCE': str(instance), 'SCENE': setup['task_instance']['scene'],
                       'RUN_DIR': str(run), 'CAMPAIGN': str(CAMPAIGN),
                       'BUDGET': str(setup['task_instance']['official_nominal_step_budget'])}.items():
        kickoff = kickoff.replace('{{' + key + '}}', value)
    (run / 'PRACTICER-KICKOFF.md').write_text(kickoff)
    print('RUN_READY', run)


def stage(task, instance, name, worker_run, zero_shot):
    run = CAMPAIGN / 'runs' / name
    if (run / 'SETUP.next.json').exists():
        raise SystemExit('A layout is already staged; let the agent consume it with admin_reset first')
    setup = {**binding(task, instance, worker_run), 'zero_shot': zero_shot}
    (run / 'SETUP.next.json').write_text(json.dumps(setup, indent=2) + '\n')
    print('STAGED', run / 'SETUP.next.json', 'zero_shot' if zero_shot else '')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('task')
    parser.add_argument('instance', type=int)
    parser.add_argument('run')
    parser.add_argument('--next', metavar='WORKER_RUN', help='Stage this READY worker run as the next layout of RUN')
    parser.add_argument('--no-zero-shot', action='store_true', help='Allow snapshots/feedback on the first attempt')
    args = parser.parse_args()
    if not 10 <= args.instance <= 300:
        parser.error('training instance 10..300 only')
    campaign()
    if args.next:
        stage(args.task, args.instance, args.run, args.next, not args.no_zero_shot)
    else:
        new_run(args.task, args.instance, args.run)
