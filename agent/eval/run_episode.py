"""Run one agent episode with the official evaluator and the agent-only server (no VLA checkpoint needed).

    python -m agent.eval.run_episode --full --native-python /path/to/evaluator/python \
        --key-file ~/.openai.env --task installing_smoke_detectors --mode train --instance 20 \
        --output runs/smoke-20 [--replay]

Without --full it is a bounded smoke test: the agent reads its notes, ends one turn on purpose (to test
same-session continuation), observes, makes one small move, and stops; the runner checks that sequence.
With --full the evaluator owns the episode and writes the official JSON and video under <output>/official.
The evaluator process never receives the API key. Linux only (uses taskset/sched_getaffinity).
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import shlex
import socket
import subprocess
import sys
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[2]


def source_revision():
    archive = ROOT/'SOURCE.json'
    if archive.exists():
        return json.loads(archive.read_text())['source_commit']
    return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()


def stop(process):
    if process is None or process.poll() is not None:return
    process.send_signal(signal.SIGTERM)
    try:process.wait(timeout=20)
    except subprocess.TimeoutExpired:
        process.kill();process.wait(timeout=5)


def wait_for_evaluator(native, server, deadline_seconds=7200):
    # Return whether the wall-time guard fired; the caller closes the evaluator.
    deadline = time.monotonic() + deadline_seconds
    while native.poll() is None and server.poll() is None:
        if time.monotonic() >= deadline:
            return True
        time.sleep(1)
    return False


def read_key_file(path):
    """Read JSON, a dotenv assignment, or a bare key without executing shell text."""
    value = path.expanduser().read_text().strip()
    if value.startswith('{'):
        key = json.loads(value).get('OPENAI_API_KEY')
    elif any(line.lstrip().startswith(('OPENAI_API_KEY=', 'export OPENAI_API_KEY='))
             for line in value.splitlines()):
        assignments = [line.strip().removeprefix('export ').partition('=')[2]
                       for line in value.splitlines()
                       if line.lstrip().startswith(('OPENAI_API_KEY=', 'export OPENAI_API_KEY='))]
        words = shlex.split(assignments[-1], comments=True)
        key = words[0] if len(words) == 1 else None
    else:
        key = value
    if not isinstance(key, str) or not key or any(c.isspace() for c in key) or '$' in key or '`' in key:
        raise ValueError('Key file must contain a literal OPENAI_API_KEY or a bare key')
    return key


def record_interruption(output, task, reason):
    """Describe an unscored, closed recording without manufacturing a native result."""
    videos = list((output/'official').rglob(task+'_*.mp4'))
    if len(videos) != 1:
        return
    instance, rollout = videos[0].stem[len(task)+1:].rsplit('_', 1)
    (output/'interruption.json').write_text(json.dumps(dict(task=task, instance_id=int(instance),
        rollout_id=int(rollout), video=str(videos[0].relative_to(output)), reason=reason), indent=2)+'\n')


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native-python',required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--task',default='hanging_pictures');p.add_argument('--instance',type=int,default=20)
    p.add_argument('--port',type=int,default=48801);p.add_argument('--seconds-after-act',type=float,default=120)
    p.add_argument('--full',action='store_true')
    p.add_argument('--key-file',type=Path,help='Read-only JSON/dotenv/bare-key file; never sourced or deleted')
    p.add_argument('--mode',choices=('train','public_test'),default='train')
    p.add_argument('--replay',action='store_true',help='Record the agent\'s model turns, tool calls and robot RPCs')
    p.add_argument('--deadline-seconds',type=float,
                   help='Wall-time guard for full runs (default: the task budget + 30 min, else 7200 s); '
                        'interrupted recordings have no official score')
    p.add_argument('--native-cwd',type=Path,help='Evaluator working directory, if its installation requires one')
    a=p.parse_args()
    if a.deadline_seconds is None:
        entry=json.loads((ROOT/'agent/tasks/tasks.json').read_text())['tasks'].get(a.task)
        a.deadline_seconds=float(entry['max_steps']+1800) if entry else 7200.
    if a.deadline_seconds <= 0:p.error('Deadline must be positive')
    a.output=a.output.resolve();a.output.mkdir(parents=True,exist_ok=False,mode=0o700)
    with socket.socket() as probe:probe.bind(('127.0.0.1',a.port))
    base_env=dict(os.environ);key=base_env.pop('OPENAI_API_KEY',None)
    if a.key_file:key=read_key_file(a.key_file)
    assert key,'Set OPENAI_API_KEY or pass --key-file'
    cpu=sorted(os.sched_getaffinity(0))[:8]
    server_env=dict(base_env,OPENAI_API_KEY=key,B1K_AGENT_RUN_ROOT=str(a.output/'forks'),
                    PATH=str(Path(sys.executable).parent)+os.pathsep+base_env.get('PATH',''),
                    B1K_AGENT_SMOKE='0' if a.full else '1',
                    B1K_AGENT_TEST_EARLY_TURN='0' if a.full else '1',
                    B1K_AGENT_EXIT_ON_DISCONNECT='1' if a.full else '0')
    if a.replay:server_env['B1K_AGENT_REPLAY']='1'
    del key
    server=native=None;started=time.monotonic();first_act=None;timed_out=False
    try:
        with (a.output/'policy.log').open('wb') as log:
            server=subprocess.Popen(['taskset','-c',','.join(map(str,cpu)),sys.executable,'-u',
                '-m','agent.eval.serve_agent_only','--port',str(a.port)],cwd=ROOT,env=server_env,stdout=log,stderr=subprocess.STDOUT)
        server_env.pop('OPENAI_API_KEY',None)
        ready_by=time.monotonic()+120  # covers the server's OpenAI preflight with its retry
        while True:
            if server.poll() is not None:raise RuntimeError('Policy server startup failed')
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{a.port}/healthz',timeout=1):break
            except OSError:
                if time.monotonic()>=ready_by:raise TimeoutError('Policy health check')
                time.sleep(.1)
        command=[a.native_python,'-u','-m','omnigibson.eval.eval','--task-name',a.task,
                 '--mode',a.mode,'--instance-indices',str(a.instance),'--num-envs','1','--num-rollouts','1',
                 '--host','127.0.0.1','--port',str(a.port),
                 '--env-wrapper','omnigibson.eval.wrappers.RGBDFullResWrapper',
                 '--output-dir',str(a.output/'official'),'--write-video']
        native_env=dict(base_env,B1K_AGENT_EVALUATOR='1')
        with (a.output/'native.log').open('wb') as log:
            native=subprocess.Popen(command,cwd=a.native_cwd or ROOT,env=native_env,stdout=log,stderr=subprocess.STDOUT)
        (a.output/'LAUNCH.json').write_text(json.dumps({'command':command,'native_pid':native.pid,
            'server_pid':server.pid,'policy_cpus':cpu,'source':source_revision(),
            'full':a.full,'replay':a.replay,'deadline_seconds':a.deadline_seconds,
            'base_checkpoint_loaded':False},indent=2)+'\n')
        if (ROOT/'SOURCE.json').exists():
            (a.output/'SOURCE.json').write_bytes((ROOT/'SOURCE.json').read_bytes())
            if (ROOT/'source.patch').exists():
                (a.output/'source.patch').write_bytes((ROOT/'source.patch').read_bytes())
        else:
            (a.output/'source.patch').write_bytes(subprocess.check_output(['git','diff','HEAD'],cwd=ROOT))
        if a.replay:
            sources = ['agent/eval/runtime.py', 'agent/eval/replay_recording.py',
                       'agent/pi/extensions/replay.ts', 'agent/eval/run_episode.py']
            (a.output/'recording-source.json').write_text(json.dumps({
                name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sources}, indent=2)+'\n')
        print('REAL_OFFICIAL_CLI_STARTED',a.task,a.instance,native.pid,flush=True)
        if a.full:
            timed_out=wait_for_evaluator(native,server,a.deadline_seconds)
        else:
            while time.monotonic()-started<1800:
                if server.poll() is not None:raise RuntimeError('Policy server exited')
                calls=[]
                for f in (a.output/'forks').glob('*/PUBLIC-CALLS.json'):
                    try:calls+=json.loads(f.read_text())
                    except (ValueError,OSError):pass
                if first_act is None and any(x.get('op')=='act' and x.get('executed_ticks',0)>0 for x in calls):
                    first_act=time.monotonic();print('REAL_OBSERVE_ACT_COMPLETED',flush=True)
                if first_act and time.monotonic()-first_act>=a.seconds_after_act:break
                if native.poll() is not None:
                    if first_act:break
                    raise RuntimeError('Native evaluator exited before a completed act')
                time.sleep(1)
            else:raise TimeoutError('Bounded qualification deadline')
            assert first_act is not None
    finally:
        if timed_out and native and native.poll() is None:
            # The evaluator's SIGINT handler finalizes its video. Keep the policy
            # bridge alive until it has stopped, so no fallback action is requested.
            native.send_signal(signal.SIGINT)
            try:native.wait(timeout=60)
            except subprocess.TimeoutExpired:stop(native)
        stop(server)  # closes bridge and reaps owned Pi
        if native and native.poll() is None:
            if a.full:
                # Allow the evaluator to finish its own shutdown after socket closure.
                try:native.wait(timeout=25)
                except subprocess.TimeoutExpired:stop(native)
            else:
                native.send_signal(signal.SIGINT)
                try:native.wait(timeout=25)
                except subprocess.TimeoutExpired:stop(native)
    if a.full:
        print('FULL_RUN_CLOSED',json.dumps({'native_returncode':native.returncode,
            'elapsed_seconds':time.monotonic()-started}),flush=True)
        results = list((a.output/'official/json').glob('*.json'))
        if not results:
            reason = ('Wall-time guard reached; evaluator finalized the video without a native score.'
                      if timed_out else 'Evaluator closed without a scored result; see the retained policy and native logs.')
            record_interruption(a.output, a.task, reason)
            if timed_out and native.returncode == 0:
                print('FULL_RUN_INTERRUPTED',json.dumps({'elapsed_seconds':time.monotonic()-started,
                    'reason':reason}),flush=True)
                return
            raise RuntimeError('No native scored result; interrupted recording retained')
        if native.returncode != 0:
            raise RuntimeError('Native evaluator exited unsuccessfully; artifacts retained')
        return  # Official evaluator artifacts own the outcome; no smoke assertions.
    forks=list((a.output/'forks').glob('*/FORK.json'));assert len(forks)==1
    run=forks[0].parent;calls=json.loads((run/'PUBLIC-CALLS.json').read_text())
    assert any(x.get('op')=='observe' for x in calls)
    assert any(x.get('op')=='act' and x.get('executed_ticks',0)>0 for x in calls)
    reads=set();images=0;responses=0
    for line in (run/'events.jsonl').open():
        try:event=json.loads(line)
        except ValueError:continue
        if event.get('type')=='tool_execution_start':
            args=event.get('args',{});text=str(args.get('path',''))+' '+str(args.get('command',''))
            if f'task_pack/{a.task}/README.md' in text:reads.add('task_pack')
            if 'NOTES.md' in text:reads.add('notes')
        if event.get('type')=='tool_execution_end':
            images+=int(event.get('result',{}).get('details',{}).get('simulatorEndpointImages',0))
        if event.get('type')=='message_end':
            m=event.get('message',{})
            if m.get('role')=='assistant' and m.get('provider')=='openai' and m.get('model')=='gpt-6-astra':responses+=1
    resumes=json.loads((run/'RESUMES.json').read_text())
    assert reads=={'task_pack','notes'} and images>=2 and responses and resumes
    result={'status':'ARCHITECTURE_SMOKE_PASS','task':a.task,'instance':a.instance,'reads':sorted(reads),
        'endpoint_images':images,'model_responses':responses,'same_session_resumes':len(resumes),
        'public_calls':calls,'elapsed_seconds':time.monotonic()-started,'seconds_after_first_act':time.monotonic()-first_act,
        'base_checkpoint_loaded':False,'full_task_success':None,'intentional_stop':not a.full}
    (a.output/'SMOKE-RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ARCHITECTURE_SMOKE_PASS',json.dumps(result),flush=True)


if __name__=='__main__':main()
