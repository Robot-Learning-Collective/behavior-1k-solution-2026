"""Practice-only worker operations (reset, finish, snapshot, restore, practice_feedback).

Called by sim_client's admin_* functions in practice; never available in evaluation. Reads one JSON job
on stdin, queues it for worker.py and prints the result.
"""
import json
import os
from pathlib import Path
import sys
import time
import uuid

work = Path(os.environ['ASTRA_WORK_DIR'])  # the worker's job queue
job = json.load(sys.stdin)
assert job['op'] in ('reset','finish','snapshot','restore','practice_feedback'), 'Unknown administrative operation'
request = f'admin_{time.time_ns()}_{uuid.uuid4().hex}'
path = work / f'{request}.job.json'
tmp = path.with_suffix('.tmp')
tmp.write_text(json.dumps(job))
tmp.replace(path)
receipt = work / f'{request}.result.json'
deadline = time.monotonic()+120
while not receipt.exists():
    if time.monotonic() >= deadline: raise TimeoutError('Worker admin RPC timed out')
    time.sleep(.1)
reply = json.loads(receipt.read_text())
if reply['status'] != 'ok': raise RuntimeError(reply.get('message', reply.get('traceback','Administrative operation failed')))
print(json.dumps(reply['result']))
