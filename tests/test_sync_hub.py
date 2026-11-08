"""Exercise sync in disposable repositories; no real hub or remote is modified."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'bin' / 'sync-hub.sh'


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.repo = root / 'hub'
        self.repo.mkdir()
        self.remote = root / 'remote.git'
        self.run_git('init', '--bare', str(self.remote))
        self.run_git('init', '-b', 'main')
        self.run_git('config', 'user.name', 'Sync Test')
        self.run_git('config', 'user.email', 'sync@example.invalid')
        for d in ('bin', 'repos', 'skills/example', 'overlays'):
            (self.repo / d).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SCRIPT, self.repo / 'bin/sync-hub.sh')
        (self.repo / 'bin/consolidate-skills.sh').write_text(
            '#!/bin/bash\nif [[ "${1:-}" == --apply ]]; then echo applied > consolidation.marker; fi\necho "scan complete"\n')
        (self.repo / 'bin/consolidate-skills.sh').chmod(0o755)
        (self.repo / 'bin/repos-lock.sh').write_text(
            '#!/bin/bash\ncd "$(dirname "$0")/.."\nprintf "# generated\\n" > repos.lock\n')
        (self.repo / '.gitignore').write_text('# BEGIN skill-lock\n# END skill-lock\n')
        (self.repo / '.skill-lock.json').write_text('{"skills":{}}\n')
        (self.repo / 'repos.lock').write_text('# generated\n')
        (self.repo / 'README.md').write_text('original\n')
        (self.repo / 'skills/example/SKILL.md').write_text('original\n')
        self.run_git('add', '.')
        self.run_git('commit', '-m', 'fixture')
        self.run_git('remote', 'add', 'origin', str(self.remote))
        self.run_git('push', '-u', 'origin', 'main')

    def run_git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], stderr=subprocess.DEVNULL)

    def sync(self, *args):
        return subprocess.run(['bash', 'bin/sync-hub.sh', *args], cwd=self.repo,
                              capture_output=True, text=True)

    def dirty(self):
        (self.repo / 'README.md').write_text('unrelated edit\n')
        (self.repo / '.orca-skill-backups').mkdir()
        (self.repo / '.orca-skill-backups/private.txt').write_text('keep local\n')
        (self.repo / 'skills/new').mkdir()
        (self.repo / 'skills/new/SKILL.md').write_text('not published\n')
        (self.repo / 'skills/example/SKILL.md').write_text('tracked edit\n')
        (self.repo / '.skill-lock.json').write_text('{"skills":{"new-source":{}}}\n')

    def test_preview_preserves_files_index_head_and_remote(self):
        self.dirty()
        before = self.run_git('status', '--porcelain', '-uall')
        head = self.run_git('rev-parse', 'HEAD')
        index = (self.repo / '.git/index').read_bytes()
        result = self.sync('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('skills/example/SKILL.md', result.stdout)
        self.assertIn('.gitignore', result.stdout)
        self.assertNotIn('README.md', result.stdout)
        self.assertEqual(before, self.run_git('status', '--porcelain', '-uall'))
        self.assertEqual(head, self.run_git('rev-parse', 'HEAD'))
        self.assertEqual(index, (self.repo / '.git/index').read_bytes())
        self.assertFalse((self.repo / 'consolidation.marker').exists())
        self.assertEqual(head, self.run_git('rev-parse', 'origin/main'))

    def test_apply_publishes_only_allowlisted_changes(self):
        self.dirty()
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        files = self.run_git('diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD').decode().splitlines()
        self.assertEqual(sorted(files), ['.gitignore', '.skill-lock.json', 'skills/example/SKILL.md'])
        self.assertEqual(self.run_git('rev-parse', 'HEAD'), self.run_git('rev-parse', 'origin/main'))
        self.assertIn(b' M README.md', self.run_git('status', '--porcelain'))
        self.assertTrue((self.repo / '.orca-skill-backups/private.txt').exists())

    def test_staged_work_blocks_before_consolidation(self):
        (self.repo / 'README.md').write_text('staged work\n')
        self.run_git('add', 'README.md')
        before = self.run_git('diff', '--cached')
        result = self.sync()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('index contains staged', result.stderr)
        self.assertEqual(before, self.run_git('diff', '--cached'))
        self.assertFalse((self.repo / 'consolidation.marker').exists())

    def test_unpushed_commit_blocks(self):
        (self.repo / 'README.md').write_text('local commit\n')
        self.run_git('add', 'README.md')
        self.run_git('commit', '-m', 'local')
        result = self.sync()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unpushed commits', result.stderr)
        self.assertFalse((self.repo / 'consolidation.marker').exists())

    def test_unknown_option_fails_without_changes(self):
        before = self.run_git('status', '--porcelain')
        result = self.sync('--unknown')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(before, self.run_git('status', '--porcelain'))


if __name__ == '__main__':
    unittest.main()
