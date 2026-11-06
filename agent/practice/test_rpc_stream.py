"""No simulator: large framed streams, cuts/corruption, recovery without redispatch."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import uuid
import os
from unittest.mock import patch
os.environ.setdefault('ASTRA_WORK_DIR', tempfile.gettempdir())
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'control'))
import rpc  # noqa: E402
import rpc_stream as stream  # noqa: E402

with tempfile.TemporaryDirectory() as directory:
    root=Path(directory).resolve()
    data=json.dumps({'payload':'é'*2_000_000},ensure_ascii=False).encode()
    (root/'payload').write_bytes(data)
    server=root/'server.py'
    server.write_text('''import hashlib,json,sys,time
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from rpc_stream import send,MAX_BYTES
root=Path(__file__).parent;mode=sys.argv[2];recovery='--read-reply' in sys.argv
if not recovery:
 job=json.loads(sys.stdin.readline())
 with (root/'dispatches').open('a') as f:f.write(job['request_id']+'\\n')
else:
 with (root/'recoveries').open('a') as f:f.write('read-only\\n')
data=(root/'payload').read_bytes()
if mode=='stall':time.sleep(3)
if (not recovery and mode in ('cut','corrupt','oversize')) or mode=='always-cut':
 digest=hashlib.sha256(data).hexdigest()
 length=MAX_BYTES+1 if mode=='oversize' else len(data)
 sys.stdout.buffer.write(f'RPC1 {length} {digest}\\n'.encode())
 sys.stdout.buffer.write((b'x'+data[1:]) if mode=='corrupt' else data[:39087])
 sys.stdout.buffer.flush()
else:
 send(data)
 (root/'acked').write_text('yes')
''')
    for mode in ('normal','cut','corrupt','oversize','always-cut','stall'):
        for p in ('dispatches','recoveries','acked'):(root/p).unlink(missing_ok=True)
        job={'op':'act','action':{},'request_id':str(uuid.uuid4())}
        command=[sys.executable,str(server),str(Path(__file__).resolve().parents[1]/'control'),mode]
        began=time.monotonic()
        try:result=stream.request(command,job,timeout=.15 if mode=='stall' else 10)
        except (ValueError,RuntimeError):assert mode in ('always-cut','stall')
        else:
            assert mode not in ('always-cut','stall') and result==data
            assert (root/'acked').read_text()=='yes'
        assert len((root/'dispatches').read_text().splitlines())==1,'Motion was replayed'
        if mode in ('cut','corrupt','oversize','always-cut'):
            assert len((root/'recoveries').read_text().splitlines())==1
        if mode=='stall':assert time.monotonic()-began<2
    # Production sanitizer/cache: private evaluator fields must never be serialized.
    request_id=str(uuid.uuid4());image=root/'observation_000001.jpg';depth=root/'observation_000001_depth.npz'
    image.write_bytes(b'image');depth.write_bytes(b'float-depth')
    obs=dict(observation_id=1,action_id=request_id,simulated_seconds=1.,wall_seconds=2.,capture_monotonic_ns=3,robot={},image=str(image),depth_file=str(depth),private_truth='TOP_SECRET_SCORER')
    obs['cameras']={name:{k:[] for k in ('intrinsics','camera_to_body','image_size_hw','camera_axes','pose_source','pixel_center_offset')} for name in ('left','head','right')}
    (root/f'{request_id}.result.json').write_text(json.dumps({'status':'ok','result':{'observation':obs,'private_truth':'TOP_SECRET_SCORER'}}))
    with patch.object(rpc,'WORK',root),patch.dict(rpc.os.environ,ASTRA_ARTIFACTS_ROOT=str(root)):
        public=rpc.policy_reply(request_id)
        assert b'TOP_SECRET_SCORER' not in public
        assert json.loads(public)['depth_sha256']==hashlib.sha256(b'float-depth').hexdigest()
        assert rpc.policy_reply(request_id)==public
    assert not list(root.glob('*.job.json')), 'Saved-reply retrieval dispatched a job'
print('PASS:4MB UTF8/ACK, cuts at39087, hash corruption, oversized headers, timeout, one-dispatch recovery, private-field exclusion')
