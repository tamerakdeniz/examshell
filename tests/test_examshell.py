import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import examshell as app
from m2.cases import FUNCTION, PROGRAM
from m2.grader import QUESTIONS, grade, initialize


class ExamTests(unittest.TestCase):
    def test_compiler_warnings_fail_before_running_cases(self):
        warnings = {
            'unused-variable': 'void warning_probe(void) { int unused; }',
            'unused-parameter': 'void warning_probe(int unused) {}',
        }
        with tempfile.TemporaryDirectory() as tmp:
            for q in ('fizzbuzz', 'ft_atoi', 'do_op'):
                for warning, code in warnings.items():
                    with self.subTest(q=q, warning=warning):
                        d = Path(tmp) / q / warning
                        p = initialize(q, d)
                        shutil.copyfile(app.solution(q), p)
                        if q == 'do_op':
                            (d / 'helper.c').write_text(code)
                        else:
                            with p.open('a') as source:
                                source.write('\n' + code + '\n')
                        with patch('m2.grader.subprocess.run', wraps=subprocess.run) as run:
                            ok, msg = grade(q, d)
                        self.assertFalse(ok, msg)
                        self.assertIn(warning, msg)
                        self.assertEqual(run.call_count, 1, 'Failed builds must not run test cases')

    def test_all_reference_solutions(self):
        self.assertEqual(set(QUESTIONS), set(FUNCTION) | set(PROGRAM))
        with tempfile.TemporaryDirectory() as tmp:
            for q in QUESTIONS:
                d=Path(tmp)/q
                p=initialize(q,d)
                for long in (False,True):
                    with self.subTest(q=q,long=long):
                        shutil.copyfile(app.solution(q,long),p)
                        ok, msg=grade(q,d)
                        self.assertTrue(ok,msg)

    def test_exam_retry_resume_and_finish(self):
        with tempfile.TemporaryDirectory() as tmp:
            home=Path(tmp)
            (home/'config.json').write_text('{"language":"tr"}')
            def run(commands):
                out=io.StringIO()
                with redirect_stdout(out),patch('builtins.input',side_effect=commands),patch('getpass.getpass',return_value=''):
                    app.shell(home)
                return out.getvalue()
            state=lambda: json.loads((home/'progress.json').read_text())
            run(['/exam','/quit'])
            q=state()['session']['question']
            path=next((home/'work').rglob('*.c'))
            path.write_text(app.solution(q).read_text() + '\nvoid warning_probe(int unused) {}\n')
            self.assertIn('Derleme hatası:',run(['/grade','/quit']))
            self.assertEqual(q,state()['session']['question'])
            self.assertEqual(state()['solved'],[])
            path.write_text('int main(void){return 0;}')
            self.assertIn('Beklenen:',run(['/grade','/quit']))
            self.assertEqual(q,state()['session']['question'])
            for level in range(1,5):
                s=state()['session'];q=s['question']
                self.assertIn(q,app.LEVELS[level])
                p=home/'work'/s['id']/str(level)/q/app.filename(q)
                shutil.copyfile(app.solution(q),p)
                run(['/grade','/quit'])
            self.assertIsNone(state()['session'])
            self.assertEqual(len(state()['solved']),4)

    def test_exit_starts_fresh_and_quit_resumes(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home/'config.json').write_text('{"language":"tr"}')
            def run(commands):
                with redirect_stdout(io.StringIO()), patch('builtins.input', side_effect=commands), patch('getpass.getpass', return_value=''):
                    app.shell(home)
                return json.loads((home/'progress.json').read_text())
            first = run(['/exam', '/quit'])['session']
            self.assertIsNone(run(['exit'])['session'])
            second = run(['/exam', '/quit'])['session']
            self.assertNotEqual(first['question'], second['question'])
            self.assertNotEqual(first['id'], second['id'])
            self.assertEqual(run(['/quit'])['session'], second)

    def test_practice(self):
        s=dict(levels=[3,1],mode='ordered',repeat=False,index=0)
        solved=set(app.LEVELS[3])
        for q in app.LEVELS[1][1:]: solved.add(q)
        self.assertEqual(app.choose(s,solved),app.LEVELS[1][0])
        solved.add(app.LEVELS[1][0])
        self.assertIsNone(app.choose(s,solved))
        s.update(repeat=True,index=0)
        self.assertIn(app.choose(s,solved),app.LEVELS[3])
        s['index']+=1
        self.assertIn(app.choose(s,solved),app.LEVELS[1])
        s.update(mode='random',levels=[4])
        self.assertIn(app.choose(s,solved),app.LEVELS[4])

    def test_ai(self):
        from m2.ai import MODELS, ask
        for model in MODELS:
            with patch('urllib.request.urlopen',return_value=io.BytesIO(b'{"candidates":[{"content":{"parts":[{"text":"ok"}]}}]}')) as send:
                self.assertEqual(ask('example',model,'hello'),'ok')
                req=send.call_args.args[0]
                self.assertIn(model+':generateContent',req.full_url)
                self.assertEqual(req.get_header('X-goog-api-key'),'example')
