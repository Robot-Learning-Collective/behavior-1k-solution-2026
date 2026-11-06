"""Integrity-checked exec replies; sender stays alive until the receiver acknowledges.
Recovery retrieves a saved public reply by UUID, never re-submits a simulator job.
"""
import hashlib
import json
import select
import subprocess
import sys
import tempfile
import threading
import time

MAX_BYTES = 64 * 1024 * 1024
VERSION = 'framed-policy-v1'


def send(data):
    if not 0 < len(data) <= MAX_BYTES:
        raise ValueError('Policy reply exceeds transport size bound')
    digest = hashlib.sha256(data).hexdigest()
    sys.stdout.buffer.write(f'RPC1 {len(data)} {digest}\n'.encode('ascii'))
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    # Do not close exec's output stream while its data may still be in transit.
    if not select.select([sys.stdin], [], [], 30)[0]:
        raise TimeoutError('Policy reply acknowledgement timed out')
    if sys.stdin.readline().strip() != 'ACK ' + digest:
        raise ValueError('Policy reply was not acknowledged')


def exchange(command, job, timeout):
    with tempfile.TemporaryFile() as errors:
        with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=errors) as p:
            timer = threading.Timer(timeout, p.kill)
            timer.daemon = True
            timer.start()
            try:
                if job is not None:
                    p.stdin.write(json.dumps(job, allow_nan=False).encode()+b'\n')
                    p.stdin.flush()
                header = p.stdout.readline(256)
                fields = header.decode('ascii').strip().split()
                if not header.endswith(b'\n') or len(fields) != 3 or fields[0] != 'RPC1':
                    raise ValueError('Missing or malformed policy transport header')
                length = int(fields[1]);digest = fields[2]
                if not 0 < length <= MAX_BYTES or len(digest) != 64:
                    raise ValueError('Invalid policy transport length/hash')
                data = p.stdout.read(length)  # Buffered read: all declared bytes or EOF.
                if len(data) != length or hashlib.sha256(data).hexdigest() != digest:
                    raise ValueError(f'Incomplete/corrupt policy reply: expected {length}, received {len(data)} bytes')
                json.loads(data)  # Reject malformed payload before acknowledging.
                p.stdin.write(('ACK '+digest+'\n').encode('ascii'))
                p.stdin.flush()
                p.stdin.close();p.stdin = None
                code = p.wait()
                if code:
                    raise RuntimeError(f'Policy transport exited {code} after complete reply')
                if p.stdout.read(1):
                    raise ValueError('Unexpected trailing policy transport bytes')
                return data
            finally:
                timer.cancel()
                if p.poll() is None:p.kill()
                p.wait()


def request(command, job, timeout=600, *, read_reply_id=None):
    """One dispatch at most; one bounded recovery of the same immutable public reply."""
    request_id = read_reply_id or job['request_id']
    deadline = time.monotonic()+timeout
    first = command+['--framed'] if read_reply_id is None else command+['--framed','--read-reply',request_id]
    try:
        return exchange(first, job if read_reply_id is None else None, timeout)
    except (OSError, ValueError, RuntimeError) as original:
        remaining = min(30., deadline-time.monotonic())
        if remaining <= 0:raise
        try:
            return exchange(command+['--framed','--read-reply',request_id], None, remaining)
        except (OSError, ValueError, RuntimeError) as recovery:
            raise RuntimeError(f'Policy transport failed; saved-reply recovery failed; motion was NOT replayed. First: {original}; recovery: {recovery}') from recovery
