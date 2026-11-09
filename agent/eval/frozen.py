"""Frozen practice contexts: where they live, how they are checked and assembled.

Every enabled task in agent/tasks/tasks.json names one frozen Pi session (the practice conversation the
agent forks at the start of each evaluation episode) and the support files copied next to it:

    agent/tasks/<task>/session.jsonl        the frozen session (not in git, see below)
    agent/tasks/<task>/NOTES.md             what the practice agent learned, written by itself
    agent/tasks/<task>/EVAL-PROCEDURE.md    optional short procedure written for evaluation
    agent/tasks/<task>/examples/...         reproducible sub-skill recipes from practice
    agent/tasks/<task>/pack/...             public task pack (copied to the run as task_pack/<task>/...)

Sessions are 29-395 MB of JSONL each, so they are stored as gzip parts below GitHub's 100 MB file limit,
and support files that are too large for git (keyframes, recorded trajectories) travel with them. Both live
in agent/frozen/ ("the bundle"):

    agent/frozen/<task>-NN.jsonl.gz         session parts
    agent/frozen/support/<task>/<name>      support files listed under "bundle" in tasks.json

`python -m agent.eval.frozen` reassembles the sessions, copies the bundle support files into place and
checks every size and SHA-256 recorded in tasks.json. `--disable-missing` instead disables (in tasks.json) every
task whose bundle files are absent, so a build without the bundle serves the learned policy for all tasks.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile

AGENT_ROOT = Path(__file__).resolve().parents[1]
REGISTRY = AGENT_ROOT / 'tasks/tasks.json'
PARTS = AGENT_ROOT / 'frozen'


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def member(root, name):
    """root/name, refusing absolute paths and anything that escapes root."""
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('Unsafe bundle member: ' + name)
    result = Path(root).joinpath(*path.parts)
    if not result.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError('Bundle member escapes root')
    return result


def support_source(task_root, task, name):
    """Repository file for a support name. Names are run-relative: NOTES.md, examples/..., task_pack/<task>/..."""
    pack = f'task_pack/{task}/'
    if name.startswith(pack):
        return member(Path(task_root) / task / 'pack', name[len(pack):])
    if name in ('NOTES.md', 'EVAL-PROCEDURE.md') or name.startswith('examples/'):
        return member(Path(task_root) / task, name)
    raise ValueError('Unexpected support member: ' + name)


def copy_checked(source, target, expected):
    if source.is_symlink() or not source.is_file():
        raise ValueError('Expected a regular frozen file: ' + str(source))
    target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with source.open('rb') as src, target.open('xb') as dst:
        target.chmod(0o600)
        shutil.copyfileobj(src, dst, 1024 * 1024)
    if sha256(target) != expected:
        raise ValueError('Hash mismatch; do not use: ' + str(target))


def materialize_task(task, session, parts_dir=PARTS, task_root=AGENT_ROOT / 'tasks'):
    destination = Path(task_root) / task / 'session.jsonl'
    if destination.exists():
        if sha256(destination) != session['sha256']:
            raise ValueError('Existing session hash mismatch: ' + task)
        return 'verified'
    fd, temporary = tempfile.mkstemp(prefix='.session-', dir=destination.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(fd, 'wb') as target:
            total = 0
            for part in session['parts']:
                path = member(parts_dir, part['name'])
                if path.stat().st_size != part['bytes'] or sha256(path) != part['sha256']:
                    raise ValueError('Frozen part integrity failure: ' + part['name'])
                with gzip.open(path, 'rb') as source:
                    while chunk := source.read(1024 * 1024):
                        total += len(chunk)
                        if total > session['bytes']:
                            raise ValueError('Oversized session: ' + task)
                        target.write(chunk)
        if total != session['bytes'] or sha256(temporary) != session['sha256']:
            raise ValueError('Reassembled session integrity failure: ' + task)
        temporary.chmod(0o444)
        os.replace(temporary, destination)
        return 'assembled'
    finally:
        temporary.unlink(missing_ok=True)


def restore_support(task, entry, parts_dir=PARTS, task_root=AGENT_ROOT / 'tasks'):
    """Copy the task's large support files from the bundle into the task directory."""
    for name in entry.get('bundle', []):
        target = support_source(task_root, task, name)
        if target.exists():
            if sha256(target) != entry['support'][name]:
                raise ValueError('Existing support hash mismatch: ' + name)
            continue
        copy_checked(member(Path(parts_dir) / 'support' / task, name), target, entry['support'][name])
        target.chmod(0o644)


def bundle_present(task, entry, parts_dir=PARTS, task_root=AGENT_ROOT / 'tasks'):
    if (Path(task_root) / task / 'session.jsonl').is_file():
        parts = True
    else:
        parts = all((Path(parts_dir) / part['name']).is_file() for part in entry['session']['parts'])
    support = all((Path(parts_dir) / 'support' / task / name).is_file() or support_source(task_root, task, name).is_file()
                  for name in entry.get('bundle', []))
    return parts and support


def materialize(registry=REGISTRY, parts_dir=PARTS, disable_missing=False):
    data = json.loads(Path(registry).read_text())
    task_root = Path(registry).parent
    for task, entry in data['tasks'].items():
        if not entry.get('enabled'):
            continue
        if disable_missing and not bundle_present(task, entry, parts_dir, task_root):
            entry['enabled'] = False
            print(task, 'DISABLED: frozen context not in the bundle; the learned policy will play it')
            continue
        restore_support(task, entry, parts_dir, task_root)
        print(task, materialize_task(task, entry['session'], parts_dir, task_root))
    if disable_missing:
        Path(registry).write_text(json.dumps(data, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--disable-missing', action='store_true')
    materialize(disable_missing=parser.parse_args().disable_missing)
