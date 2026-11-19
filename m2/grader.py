"""Compile and run the learner's own local C code (not a security sandbox)."""
from .i18n import t
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import tempfile

from .cases import DRIVERS, FUNCTION, PROGRAM

BANK = Path(__file__).resolve().parent.parent / 'bank'
QUESTIONS = {p.parent.name: p.parent for p in sorted(BANK.glob('level*/*/README.md'))}
FILES = {'hiddenp': 'hidenp.c', 'sort_in_tab': 'sort_int_tab.c'}


def filename(name):
    return FILES.get(name, name + '.c')


def initialize(name, directory):
    directory.mkdir(parents=True, exist_ok=True)
    for h in QUESTIONS[name].glob('*.h'):
        if not (directory / h.name).exists():
            shutil.copyfile(h, directory / h.name)
    path = directory / filename(name)
    path.touch(exist_ok=True)
    return path


def run_limits():
    resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def grade(name, directory):
    sources = (sorted(directory.glob('*.c')) if name in ('do_op','flood_fill')
               else [directory / filename(name)])
    if not sources or not all(p.is_file() for p in sources):
        return False, t('Teslim dosyası eksik: ') + filename(name)
    cc = shutil.which('cc')
    if not cc:
        return False, t('C derleyicisi bulunamadı: cc (Clang veya GCC) kur.')
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        binary = root / 'submission'
        if name in DRIVERS:
            driver = root / 'driver.c'
            driver.write_text(DRIVERS[name])
            sources.append(driver)
        cmd = [cc, '-std=c99', '-I', str(directory.resolve()), *[str(p.resolve()) for p in sources], '-o',str(binary)]
        try:
            build = subprocess.run(cmd,cwd=root,capture_output=True,timeout=20)
        except subprocess.TimeoutExpired:
            return False, t('Derleme zaman aşımı.')
        if build.returncode:
            return False, t('Derleme hatası:\n')+build.stderr[:4000].decode(errors='replace')
        cases = FUNCTION[name] if name in FUNCTION else PROGRAM[name]
        for i,(args,expected) in enumerate(cases,1):
            title = t('Test {0}/{1} · {2} · girdi: {3}' ,i, len(cases), name, json.dumps(args,ensure_ascii=False))
            with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
                try:
                    proc = subprocess.run([str(binary),*args],cwd=root,stdin=subprocess.DEVNULL,
                                          stdout=out,stderr=err,timeout=2,preexec_fn=run_limits,
                                          env={'PATH':os.defpath,'LC_ALL':'C'})
                    status = proc.returncode
                except subprocess.TimeoutExpired:
                    status = t('zaman aşımı (2 sn)')
                out.seek(0)
                actual = out.read()
                if status or actual != expected.encode():
                    err.seek(0)
                    detail = err.read(1500).decode(errors="replace")
                    return False, (t('{0}\nBeklenen: {1}\nAlınan:   {2}' ,title, repr(expected), repr(actual[:3000].decode(errors="backslashreplace")))
                                   + (t('\nÇıkış: {0}' ,status) if status else '')
                                   + (f'\nstderr: {detail!r}' if detail else ''))
        return True, t('{0}/{1} test geçti.' ,len(cases), len(cases))
