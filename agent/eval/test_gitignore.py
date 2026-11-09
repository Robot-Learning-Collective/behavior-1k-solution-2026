"""Every file the frozen bundle restores into the repository must be ignored by git."""
import json
from pathlib import Path
import shutil
import subprocess
import unittest

from agent.eval.frozen import AGENT_ROOT, REGISTRY, support_source

REPO = AGENT_ROOT.parent


def generated_paths():
    tasks = json.loads(REGISTRY.read_text())['tasks']
    paths = []
    for task, entry in tasks.items():
        paths.append(AGENT_ROOT / 'tasks' / task / 'session.jsonl')
        paths += [support_source(AGENT_ROOT / 'tasks', task, name) for name in entry.get('bundle', [])]
    paths.append(AGENT_ROOT / 'frozen' / 'example-01.jsonl.gz')
    return [str(p.relative_to(REPO)) for p in paths]


@unittest.skipUnless(shutil.which('git') and (REPO / '.git').exists(), 'needs git and a checkout')
class GitignoreTest(unittest.TestCase):
    def test_bundle_files_are_ignored(self):
        paths = generated_paths()
        result = subprocess.run(['git', 'check-ignore', '--no-index', '--stdin'], cwd=REPO, text=True,
                                input='\n'.join(paths) + '\n', capture_output=True)
        ignored = set(result.stdout.split())
        missing = [p for p in paths if p not in ignored]
        self.assertEqual(missing, [], 'add these to .gitignore')

    def test_bundle_files_are_not_tracked(self):
        tracked = subprocess.run(['git', 'ls-files', '--', *generated_paths()], cwd=REPO, text=True,
                                 capture_output=True, check=True).stdout.split()
        self.assertEqual(tracked, [])


if __name__ == '__main__':
    unittest.main()
