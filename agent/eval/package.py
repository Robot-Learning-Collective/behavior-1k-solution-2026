"""Freeze a practice session into the agent registry (agent/tasks/tasks.json).

    python -m agent.eval.package --task clean_a_trumpet --max-steps 7960 --task-id 37 \
        --session <pi session .jsonl> --run-dir <practice run dir> --pack <task pack dir> \
        --env-file <file with OPENAI_API_KEY=...>

What it does:
  1. Refuses the session if it contains the runtime API key or credential-shaped text (agent/eval/scrub.py).
     The scan is bounded: it does not prove that a transcript is free of private context.
  2. Splits the session into gzip parts below 80 MB (agent/frozen/<task>-NN.jsonl.gz).
  3. Copies NOTES.md, EVAL-PROCEDURE.md (if present) and examples/ from the run, and the public task pack.
     Small text files go to agent/tasks/<task>/; large or binary files go to agent/frozen/support/<task>/.
  4. Writes the task's entry: session hash, size and parts, plus the hash of every support file.
The task stays disabled until you set "enabled": true.
"""
import argparse
import collections
import gzip
import json
from pathlib import Path
import shlex
import shutil

from .frozen import PARTS, REGISTRY, member, sha256, support_source
from .scrub import scrub, scrub_text

PART_BYTES = 80_000_000
GIT_MAX_BYTES = 100_000
TEXT_SUFFIXES = ('.md', '.py', '.json')


def read_key(env_file):
    for line in Path(env_file).read_text().splitlines():
        if line.startswith('OPENAI_API_KEY='):
            return shlex.split(line.split('=', 1)[1])[0].encode()
    raise ValueError('No OPENAI_API_KEY in ' + str(env_file))


def split_session(task, session, key, parts_dir=PARTS):
    parts, block, size, redactions = [], bytearray(), 0, collections.Counter()
    parts_dir.mkdir(parents=True, exist_ok=True)

    def flush():
        path = parts_dir / f'{task}-{len(parts):02d}.jsonl.gz'
        with path.open('xb') as raw, gzip.GzipFile(filename='', fileobj=raw, mode='wb', mtime=0, compresslevel=9) as out:
            out.write(block)
        parts.append({'name': path.name, 'bytes': path.stat().st_size, 'sha256': sha256(path)})
        block.clear()

    with Path(session).open('rb') as stream:
        for line in stream:
            if key in line:
                raise ValueError('Runtime API key found in the session; refusing to package')
            if line.strip():
                scrub(json.loads(line), redactions)
            if redactions:
                raise ValueError('Credential-shaped content in the session; review it before packaging')
            if block and len(block) + len(line) > PART_BYTES:
                flush()
            block.extend(line)
            size += len(line)
    if block:
        flush()
    return {'sha256': sha256(session), 'bytes': size, 'parts': parts}


def support_files(task, run_dir, pack_dir):
    """{run-relative name: source path} for notes, examples and the task pack."""
    run_dir, files = Path(run_dir), {}
    for name in ('NOTES.md', 'EVAL-PROCEDURE.md'):
        if (run_dir / name).is_file():
            files[name] = run_dir / name
    for path in sorted((run_dir / 'examples').rglob('*')) if (run_dir / 'examples').is_dir() else []:
        if path.is_file() and not path.is_symlink():
            files[path.relative_to(run_dir).as_posix()] = path
    for path in sorted(Path(pack_dir).rglob('*')):
        if path.is_file() and not path.is_symlink():
            files[f'task_pack/{task}/' + path.relative_to(pack_dir).as_posix()] = path
    if 'NOTES.md' not in files:
        raise ValueError('The practice run has no NOTES.md')
    return files


def package(task, task_id, max_steps, session, run_dir, pack_dir, key, registry=REGISTRY, parts_dir=PARTS):
    if not task.replace('_', '').isalnum():
        raise ValueError('Bad task name: ' + task)
    data = json.loads(Path(registry).read_text())
    if task in data['tasks']:
        raise ValueError(f'{task} is already packaged; remove its entry and files first')
    task_root = Path(registry).parent
    support, bundle = {}, []
    for name, source in support_files(task, run_dir, pack_dir).items():
        raw = source.read_bytes()
        if key in raw:
            raise ValueError('Runtime API key found in support file ' + name)
        counts = collections.Counter()
        try:
            scrub_text(raw.decode(), counts)
        except UnicodeDecodeError:
            pass
        if counts:
            raise ValueError('Credential-shaped content in support file ' + name)
        large = source.suffix not in TEXT_SUFFIXES or len(raw) > GIT_MAX_BYTES
        target = member(Path(parts_dir) / 'support' / task, name) if large else support_source(task_root, task, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        support[name] = sha256(target)
        if large:
            bundle.append(name)
    data['tasks'][task] = {'task_id': task_id, 'enabled': False, 'max_steps': max_steps,
                           'session': split_session(task, session, key, Path(parts_dir)),
                           'support': dict(sorted(support.items())), 'bundle': sorted(bundle)}
    Path(registry).write_text(json.dumps(data, indent=1) + '\n')
    print(f'Packaged {task}: {len(support)} support files ({len(bundle)} in the bundle); still disabled.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--task', required=True)
    parser.add_argument('--task-id', type=int, required=True, help='Official BEHAVIOR task id')
    parser.add_argument('--max-steps', type=int, required=True, help='Official step budget (= wall seconds)')
    parser.add_argument('--session', type=Path, required=True, help='Frozen Pi session (.jsonl)')
    parser.add_argument('--run-dir', type=Path, required=True, help='Practice run with NOTES.md and examples/')
    parser.add_argument('--pack', type=Path, required=True, help='Public task pack directory')
    parser.add_argument('--env-file', type=Path, required=True, help='File with the runtime OPENAI_API_KEY line')
    args = parser.parse_args()
    if args.env_file.stat().st_mode & 0o077:
        parser.error('--env-file must not be readable by group/others (chmod 600)')
    package(args.task, args.task_id, args.max_steps, args.session, args.run_dir, args.pack, read_key(args.env_file))
