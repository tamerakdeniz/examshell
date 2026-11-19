"""Connect one ExamShell session to its own VS Code window."""
from .i18n import t, language
import json
from pathlib import Path
import select
import shutil
import subprocess
import sys
import time
import uuid

EXTENSION = Path(__file__).resolve().parent.parent / 'vscode'


class Editor:
    def __init__(self, save):
        self.save = save
        self.root = None
        self.ticket = None
        self.view = {}
        self.process = None

    def open(self, root, submission, subject, short, long):
        cli = shutil.which('code')
        if not cli:
            mac = Path('/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code')
            if not mac.is_file():
                print(t('VS Code bulunamadı. Terminal modu açık.'))
                return False
            cli = str(mac)
        previously_opened = (root/'.m2-view.json').is_file()
        self.root = root
        self.ticket = str(submission.relative_to(root))
        self.view = dict(language=language(), attempt=uuid.uuid4().hex, ticket=self.ticket, subject=subject.read_text(),
                         short=short.read_text(), long=long.read_text())
        self.display('subject')
        def acknowledged(seconds):
            deadline = time.monotonic() + seconds
            while time.monotonic() < deadline:
                try:
                    if (root/'.m2-ready').read_text() == self.revision:
                        return True
                except FileNotFoundError:
                    pass
                time.sleep(0.05)
            return False

        if previously_opened and acknowledged(2):
            return True
        try:
            self.process = subprocess.Popen(
                [cli, '--new-window', f'--extensionDevelopmentPath={EXTENSION}', str(root)],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except OSError as error:
            print(t('VS Code açılamadı: {0}' ,error))
            self.close()
            return False
        if acknowledged(12):
            return True
        print(t('VS Code güncel dosyayı henüz açmadı. Terminalden devam edebilir veya /subject ile tekrar deneyebilirsin.'))
        self.close()
        return False

    def display(self, action, long=False):
        self.revision = uuid.uuid4().hex
        self.save(self.root/'.m2-view.json', dict(self.view, action=action, alternative=long,
                                                  revision=self.revision))

    def close(self):
        if self.root:
            self.display('closed')
            (self.root/'.m2-ready').unlink(missing_ok=True)
        self.root = self.ticket = None

    def command(self, prompt):
        if not self.root:
            return input(prompt)
        print(prompt, end='', flush=True)
        request = self.root/'.m2-grade.json'
        while True:
            if self.process and self.process.poll() not in (None,0):
                print(t('VS Code açılamadı. /subject ile yeniden deneyebilirsin.'))
                self.close()
                return input(prompt)
            if request.exists():
                data = json.loads(request.read_text())
                request.unlink()
                if data.get('ticket') == self.ticket and data.get('attempt') == self.view['attempt']:
                    print('Grade')
                    return '/grade'
            if select.select([sys.stdin], [], [], 0.2)[0]:
                return input()

    def report(self, ok, message):
        self.save(self.root/'.m2-result.json',dict(ok=ok, message=message, ticket=self.ticket,
                                                  revision=uuid.uuid4().hex))
