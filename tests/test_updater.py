import io
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import tempfile
import unittest

from m2 import updater


class UpdateTests(unittest.TestCase):
    def test_update_and_local_changes(self):
        def git(*args):
            return subprocess.run(['git', *map(str, args)], check=True,
                                  capture_output=True, text=True).stdout.strip()

        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            root = Path(tmp)
            remote, source, install = [root/name for name in ('remote', 'source', 'install')]
            git('init', '--bare', remote)
            git('init', '-b', 'main', source)
            git('-C', source, 'config', 'user.name', 'Test')
            git('-C', source, 'config', 'user.email', 'test@example.com')
            (source/'version').write_text('one')
            git('-C', source, 'add', '.')
            git('-C', source, 'commit', '-m', 'first')
            git('-C', source, 'remote', 'add', 'origin', remote)
            git('-C', source, 'push', 'origin', 'main')
            git('clone', '-b', 'main', remote, install)
            self.assertEqual(updater.check(install)[1], 0)
            (source/'version').write_text('two')
            git('-C', source, 'commit', '-am', 'second')
            git('-C', source, 'push', 'origin', 'main')
            self.assertEqual(updater.check(install)[1], 1)
            (install/'version').write_text('local')
            updater.update(install)
            self.assertEqual((install/'version').read_text(), 'local')
            git('-C', install, 'restore', 'version')
            with self.assertRaises(updater.Updated):
                updater.update(install)
            self.assertEqual((install/'version').read_text(), 'two')
            updater.update(install)
            git('-C', install, 'checkout', '-b', 'feature')
            updater.update(install)
            self.assertEqual(git('-C', install, 'branch', '--show-current'), 'feature')

    def test_non_git_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(updater.UpdateError):
                updater.check(Path(tmp))
