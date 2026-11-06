"""observe/act RPC to the practice worker through its file queue (the only two operations the agent may call).

The reply carries only public observation fields (RGB-D, proprioception, camera calibration, execution
receipt); the worker's private result file, with simulator truth, never leaves this process. In framed
mode (rpc_stream.py) a lost reply is re-read by request id, never re-sent as motion.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import uuid

WORK = Path(os.environ['ASTRA_WORK_DIR'])  # the worker's job queue


def policy_reply(request_id):
    cached = WORK / f'{request_id}.policy.json'
    if cached.exists():
        return cached.read_bytes()
    reply = json.loads((WORK / f'{request_id}.result.json').read_text())
    if reply.get('status') == 'invalid_action':
        policy = {'error':'Rejected motion without actuation: '+reply['message'],'fatal':False}
    elif reply.get('status') != 'ok':
        policy = {'error':'Simulator command failed; trial stopped; runner has diagnostic receipt.','fatal':True}
    else:
        result = reply['result']
        observation = result['observation']
        image = Path(observation['image'])
        artifacts = Path(os.environ.get('ASTRA_ARTIFACTS_ROOT', str(WORK.parent / 'artifacts'))).resolve()
        if artifacts not in image.resolve().parents or not image.name.startswith('observation_') or image.suffix != '.jpg':
            raise ValueError('Image outside owned policy-observation artifacts')
        policy = {key: observation[key] for key in (
            'observation_id', 'action_id', 'simulated_seconds', 'wall_seconds', 'capture_monotonic_ns', 'robot')}
        for key in ('image_layout', 'controller_protocol', 'attempt_id', 'execution', 'act_result', 'last_commanded_grip'):
            if key in observation:
                policy[key] = observation[key]
        policy['cameras'] = {name:{key:observation['cameras'][name][key] for key in (
            'intrinsics','camera_to_body','image_size_hw','camera_axes','pose_source','pixel_center_offset')}
            for name in ('left','head','right')}
        depth = Path(observation['depth_file'])
        if (depth.resolve().parent != image.resolve().parent
                or depth.name != f"observation_{observation['observation_id']:06}_depth.npz"
                or depth.stat().st_size > 16_000_000 or image.stat().st_size > 16_000_000):
            raise ValueError('Image/depth outside matching owned endpoint artifacts / size limit')
        data = depth.read_bytes()
        policy['depth_npz_base64'] = base64.b64encode(data).decode()
        policy['depth_sha256'] = hashlib.sha256(data).hexdigest()
        policy['image_base64'] = base64.b64encode(image.read_bytes()).decode()
        policy['ended'] = result.get('ended', False)
    data = json.dumps(policy, allow_nan=False).encode()
    tmp = WORK / f'{request_id}.{os.getpid()}.policy.tmp'
    with tmp.open('xb') as f:
        os.chmod(tmp,0o600)
        f.write(data)
    tmp.replace(cached)
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--framed',action='store_true')
    group = ap.add_mutually_exclusive_group()
    group.add_argument('--read-reply')
    group.add_argument('--cancel')
    args = ap.parse_args()
    if args.cancel:
        (WORK / f'{str(uuid.UUID(args.cancel))}.cancel').touch()
        return
    if args.read_reply:
        request_id = str(uuid.UUID(args.read_reply))
    else:
        job = json.loads(sys.stdin.readline()) if args.framed else json.load(sys.stdin)
        if set(job) != {'op', 'action', 'request_id'} or job['op'] not in ('act', 'observe'):
            raise ValueError('Only act/observe are policy operations')
        request_id = str(uuid.UUID(job['request_id']))
        target = WORK / f'{request_id}.job.json'
        if target.exists() or (WORK/f'{request_id}.job.done').exists() or (WORK/f'{request_id}.result.json').exists():
            raise ValueError('Request UUID already submitted; retrieve its reply instead of replaying motion')
        temporary = target.with_suffix('.tmp')
        temporary.write_text(json.dumps(job, allow_nan=False))
        temporary.replace(target)

        def cancel(_signum, _frame):
            (WORK / f'{request_id}.cancel').touch()
            raise SystemExit(130)

        signal.signal(signal.SIGTERM, cancel)
        signal.signal(signal.SIGINT, cancel)
    deadline = time.monotonic() + 180
    receipt = WORK / f'{request_id}.result.json'
    while not receipt.exists():
        if time.monotonic() >= deadline:
            if not args.read_reply:cancel(None,None)
            raise TimeoutError('Saved policy reply not available; no motion was replayed')
        time.sleep(.1)  # Bounded lifetime of this one RPC/retrieval.
    data = policy_reply(request_id)
    if args.framed:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'control'))
        from rpc_stream import send
        send(data)
    else:
        sys.stdout.buffer.write(data+b'\n')
        sys.stdout.buffer.flush()


if __name__ == '__main__':
    main()
