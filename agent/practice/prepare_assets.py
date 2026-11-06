"""Extract only this demo's asset dependencies via bounded HTTP ZIP ranges."""
import argparse
import collections
import h5py
import io
import json
from pathlib import Path
import urllib.request
import zipfile

REVISION = '9f0d57d465726976ed98138d3f8b8ca3e2186775'
BASE = f'https://huggingface.co/datasets/behavior-1k/zipped-datasets/resolve/{REVISION}/'
ARCHIVES = {'behavior-1k-assets-3.9.0.zip': 31_457_673_073,
            'omnigibson-robot-assets-3.8.2.zip': 641_004_353,
            '2026-challenge-task-instances.zip': 108_543_852}
BLOCK = 1_048_576


class Ranges(io.RawIOBase):
    def __init__(self, url, size, max_fetched_bytes=2_000_000_000):
        self.url, self.size, self.pos = url, size, 0
        self.max_fetched_bytes = max_fetched_bytes
        self.blocks = collections.OrderedDict()
        self.fetched = 0
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self, offset, whence=0):
        self.pos = offset + (self.pos if whence == 1 else self.size if whence == 2 else 0)
        if not 0 <= self.pos <= self.size: raise ValueError('Invalid ZIP seek')
        return self.pos
    def readinto(self, buffer):
        end, written = min(self.size, self.pos + len(buffer)), 0
        while self.pos < end:
            block = self.pos // BLOCK
            if block not in self.blocks:
                first, last = block * BLOCK, min(self.size, (block + 1) * BLOCK) - 1
                request = urllib.request.Request(self.url + f'?range_block={block}', headers={'Range': f'bytes={first}-{last}'})
                with urllib.request.urlopen(request, timeout=60) as response:
                    if response.status != 206: raise ValueError('Server ignored ZIP range')
                    data = response.read(BLOCK + 1)
                if len(data) != last - first + 1: raise ValueError('Invalid ZIP range size')
                self.fetched += len(data)
                if self.fetched > self.max_fetched_bytes: raise ValueError(f'Task asset transfer exceeded {self.max_fetched_bytes} byte bound')
                self.blocks[block] = data
                if len(self.blocks) > 64: self.blocks.popitem(last=False)
            data = self.blocks[block][self.pos % BLOCK:min(BLOCK, end - block * BLOCK)]
            buffer[written:written+len(data)] = data
            self.pos += len(data)
            written += len(data)
        return written


def selected(name, kind, models):
    parts = Path(name).parts
    if parts and parts[0] in ('behavior-1k-assets', 'omnigibson-robot-assets', '2026-challenge-task-instances'):
        parts = parts[1:]
    if not parts: return False
    if parts[0] in ('VERSION', 'metadata'): return True
    if kind.startswith('behavior'):
        if parts[0] == 'systems':
            return len(parts) == 3 and parts[-1] == 'metadata.json'
        return (len(parts) >= 3 and parts[0] == 'objects' and (parts[1], parts[2]) in models) or (
            len(parts) >= 2 and parts[:2] == ('scenes', 'house_double_floor_upper') and
            ('json' not in parts or 'boxing_books_up_for_storage' in name))
    if kind.startswith('omnigibson'):
        return len(parts) >= 2 and parts[0] == 'models' and parts[1] in ('r1pro','background')
    return len(parts) >= 3 and parts[:2] == ('scenes', 'house_double_floor_upper') and 'boxing_books_up_for_storage' in name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    with h5py.File(args.raw) as f:
        scene = json.loads(f['data'].attrs['scene_file'])
    models = {(entry['args']['category'], entry['args']['model']) for entry in scene['objects_info']['init_info'].values()
              if entry['args'].get('category') and entry['args'].get('model')}
    manifest = {'revision': REVISION, 'models': sorted(models), 'archives': []}
    args.output.mkdir(parents=True, exist_ok=True)
    for name, size in ARCHIVES.items():
        stream = Ranges(BASE+name, size)
        with zipfile.ZipFile(stream) as archive:
            entries = [entry for entry in archive.infolist() if not entry.is_dir() and selected(entry.filename, name, models)]
            expanded = sum(e.file_size for e in entries)
            if expanded > 1_000_000_000: raise ValueError(f'Task selection unexpectedly exceeds1GB: {name}')
            print('ASSET_SELECTION', name, len(entries), expanded, flush=True)
            for entry in entries:
                root = ('behavior-1k-assets' if name.startswith('behavior') else 'omnigibson-robot-assets' if name.startswith('omnigibson') else '2026-challenge-task-instances')
                relative = Path(entry.filename)
                destination = args.output / (relative if relative.parts[0] == root else Path(root) / relative)
                if args.output.resolve() not in destination.resolve().parents: raise ValueError('Unsafe ZIP path')
                if destination.exists() and destination.stat().st_size == entry.file_size: continue
                destination.parent.mkdir(parents=True, exist_ok=True)
                data = archive.read(entry)  # zipfile validates CRC.
                destination.write_bytes(data)
        manifest['archives'].append({'name': name, 'selected_files': len(entries), 'expanded_bytes': expanded, 'fetched_bytes': stream.fetched})
        print('ASSET_EXTRACTED', name, stream.fetched, flush=True)
    (args.output / 'behavior-1k-assets/systems').mkdir(parents=True, exist_ok=True)
    (args.output / 'asset-selection.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('ASSETS_READY', args.output, flush=True)


if __name__ == '__main__': main()
