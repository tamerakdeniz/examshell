import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import examshell as app
from m2 import i18n
from m2.grader import QUESTIONS, grade, initialize


class LanguageTests(unittest.TestCase):
    def tearDown(self):
        i18n.set_language('en')

    def test_first_run_default_and_persistence(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            home = Path(tmp)
            with patch('builtins.input', return_value=''):
                app.load_language(home)
            self.assertEqual(i18n.language(), 'en')
            with patch('builtins.input', side_effect=AssertionError('must not prompt again')):
                app.load_language(home)
            config = json.loads((home/'config.json').read_text())
            self.assertTrue(app.configure_language(config, home/'config.json', 'tr'))
            i18n.set_language('en')
            with patch('builtins.input', side_effect=AssertionError('must not prompt again')):
                app.load_language(home)
            self.assertEqual(i18n.language(), 'tr')
            self.assertFalse(app.configure_language(config, home/'config.json', 'invalid'))
            self.assertEqual(i18n.language(), 'tr')

    def test_live_switch_preserves_session_and_editor_gets_language(self):
        class Editor:
            root = None
            def __init__(self, commands):
                self.commands = iter(commands)
                self.subjects = []
            def command(self, prompt):
                return next(self.commands)
            def open(self, root, submission, subject, short, long):
                self.subjects.append((submission, subject, i18n.language()))
                return True
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            home = Path(tmp)
            (home/'config.json').write_text('{"language":"en","onboarded":true}')
            editor = Editor(['/exam', '/lang tr', '/lang en', '/quit'])
            app.shell(home, editor)
            self.assertEqual([x[2] for x in editor.subjects], ['en','tr','en'])
            self.assertEqual(len({x[0] for x in editor.subjects}), 1)
            self.assertEqual(editor.subjects[1][1].name, 'subject.tr.txt')
            self.assertEqual(json.loads((home/'config.json').read_text())['language'], 'en')

    def test_subjects_and_help(self):
        for lang in ('en','tr'):
            i18n.set_language(lang)
            for directory in QUESTIONS.values():
                subject = i18n.subject_path(directory).read_text()
                self.assertIn('## Konu' if lang == 'tr' else '## Subject', subject)
                self.assertIn('Beklenen dosyalar' if lang == 'tr' else 'Expected files', subject)
            for command in ('/lang', '/update', '/help', '/quit', '/exam', '/practice'):
                self.assertIn(command, i18n.t(app.HELP))

    def test_grade_language(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            source = initialize('first_word', directory)
            source.write_text('int main(void){return 0;}')
            for lang, label in [('en', 'Expected:'), ('tr', 'Beklenen:')]:
                i18n.set_language(lang)
                ok, message = grade('first_word', directory)
                self.assertFalse(ok)
                self.assertIn(label, message)

    def test_milestone_language_command(self):
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()) as out:
            home = Path(tmp)
            with patch('builtins.input', side_effect=['/lang tr', '/help', 'exit']):
                self.assertIsNone(app.select_milestone(home))
            self.assertIn('Arayüz ve subject dilini değiştir', out.getvalue())
