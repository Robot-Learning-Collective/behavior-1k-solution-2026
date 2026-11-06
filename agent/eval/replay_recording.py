"""Optional, append-only evidence for educational episode replay (no policy inputs)."""
import json
import base64
import hashlib
import os
from pathlib import Path
import threading
import time

from .scrub import scrub


class ReplayRecorder:
    def __init__(self, folder, epoch):
        self.path = Path(folder) / 'robot-events.jsonl'
        self.epoch = epoch
        self.lock = threading.Lock()
        self.key = os.environ.get('OPENAI_API_KEY', '')

    def _media(self, result):
        """Copy display evidence without modifying the RPC response or duplicating blobs."""
        if not isinstance(result, dict):
            return result
        result = dict(result)
        for field, kind, extension in [('image_base64', 'image', 'jpg'),
                                       ('depth_npz_base64', 'attachment', 'npz')]:
            encoded = result.pop(field, None)
            if encoded:
                blob = base64.b64decode(encoded, validate=True)
                name = hashlib.sha256(blob).hexdigest() + '.' + extension
                folder = self.path.parent / 'replay-media'
                folder.mkdir(exist_ok=True)
                target = folder / name
                if not target.exists():
                    target.write_bytes(blob)
                result[field.removesuffix('_base64')] = dict(type=kind, path='replay-media/' + name)
        return result

    def emit(self, event, **fields):
        record = scrub(dict(schema_version=1, event=event, epoch=self.epoch,
                            wall_unix_ns=time.time_ns(), monotonic_ns=time.monotonic_ns(), **fields))
        raw = json.dumps(record, allow_nan=False, default=lambda x: x.tolist())
        if self.key:
            raw = raw.replace(self.key, '[REDACTED_CREDENTIAL]')
        with self.lock, self.path.open('a') as stream:
            stream.write(raw + '\n')

    def rpc(self, original, job):
        self.emit('robot_call_start', request_id=job['request_id'], op=job['op'],
                  arguments=job.get('action'))
        try:
            result = original(job)
        except Exception as exc:
            self.emit('robot_call_error', request_id=job['request_id'], error=str(exc))
            raise
        self.emit('robot_call_end', request_id=job['request_id'], op=job['op'], result=self._media(result))
        return result
