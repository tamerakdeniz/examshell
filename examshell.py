#!/usr/bin/env python3
"""42 Milestone 2 — yerel sınav ve pratik terminali."""
import argparse
import difflib
import getpass
import json
import os
from pathlib import Path
import random
import tempfile
import uuid

from m2.editor import Editor
from m2.ai import MODELS, ask
from m2.grader import QUESTIONS, grade, initialize, filename

LEVELS = {i: [q for q,p in QUESTIONS.items() if p.parent.name == f'level{i}'] for i in range(1,5)}
HELP = """
  /exam                         Sınav: her levelden bir rastgele soru
  /practice                     Level, sıra ve tekrar seçeneklerini belirle
  /subject  /path               Soruyu veya teslim yolunu göster
  /grade                        Kodu derle ve test et (grademe de geçerli)
  /answer [long]  /diff [long]   Kısa/uzun çözümü göster veya kodunla karşılaştır
  /progress                     Level bazında çözülen soru sayıları
  /api-key  /model              Gemini anahtarını veya modeli değiştir
  /ai <soru>                    Subject, teslim ve son test sonucuyla yardım al
  /end                          Oturumu bitir, dosyalarını sakla
  exit                          Oturumu bitir ve çık
  /quit                         Kaydet ve çık; sonraki açılışta devam et
"""


def save(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w',dir=path.parent,delete=False) as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    os.replace(f.name,path)


def read(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def choose(session, solved, previous=None):
    def pick(level, candidates):
        last = (previous or {}).get(str(level))
        return random.choice([q for q in candidates if q != last] or candidates)

    levels = session['levels']
    idx = session['index']
    if session['mode']=='exam':
        return pick(levels[idx], LEVELS[levels[idx]]) if idx<len(levels) else None
    pools = {l:[q for q in LEVELS[l] if session['repeat'] or q not in solved] for l in levels}
    available = [l for l in levels if pools[l]]
    if not available:
        return None
    if session['mode']=='random':
        level = random.choice(available)
    else:
        level = next(levels[(idx+k)%len(levels)] for k in range(len(levels)) if pools[levels[(idx+k)%len(levels)]])
        session['index'] = levels.index(level)
    return pick(level, pools[level])


def solution(name, long=False):
    d = QUESTIONS[name]
    return d/(name+'.c') if long else next(p for p in (d/'main.py',d/'main.c') if p.exists())


def practice():
    raw = input('Leveller (örn. 2 veya 1,3,4): ').strip()
    try:
        levels = list(dict.fromkeys(int(x) for x in raw.replace(',',' ').split()))
        if not levels or any(l not in LEVELS for l in levels):
            raise ValueError
    except ValueError:
        print('1 ile 4 arasında level gir.')
        return None
    mode = 'ordered'
    if len(levels)>1:
        choice = input('1: girilen sırayla · 2: rastgele [1]: ').strip()
        if choice not in ('','1','2'):
            print('Geçersiz seçim.'); return None
        mode = 'random' if choice=='2' else 'ordered'
    repeat=input('Çözülmüş sorular tekrar gelebilsin mi? [e/H]: ').strip().lower()
    if repeat not in ('','h','hayır','e','evet'):
        print('e veya h gir.'); return None
    return dict(mode=mode,levels=levels,repeat=repeat in ('e','evet'))


def configure_key(config, path):
    key = getpass.getpass('Gemini API anahtarı (gizli; Enter: atla): ').strip()
    if key:
        config['key']=key
        print('Anahtar kaydedildi.')
    config['onboarded']=True
    save(path, config)


def shell(home, editor=None):
    cfgpath, statepath = home/'config.json',home/'progress.json'
    cfg=read(cfgpath,{})
    state=read(statepath,{'solved':[], 'session':None})
    previous = state.setdefault('previous', {})
    def remember(q):
        previous[QUESTIONS[q].parent.name.removeprefix('level')] = q
    if state['session']:
        remember(state['session']['question'])
    print('42 / M2 ExamShell    •    4 level · 53 soru\n/exam: sınav   /practice: pratik   /help: komutlar')
    if not cfg.get('onboarded'):
        configure_key(cfg,cfgpath)

    def directory(s):
        return home/'work'/s['id']/str(s['passed']+1)/s['question']

    def show(s):
        q=s['question']
        path=initialize(q,directory(s))
        if editor and editor.open(home/'work', path, QUESTIONS[q]/'README.md',
                                  solution(q), solution(q, True)):
            print(f"[{QUESTIONS[q].parent.name} · {q}] VS Code'a gönderildi. Teslim: {path}")
            return
        print(f"\n[{QUESTIONS[q].parent.name} · {q}]\n{(QUESTIONS[q]/'README.md').read_text()}\nTeslim: {path}\nKaydettikten sonra /grade yaz.")

    def advance(s):
        s['last']=''
        s['question']=choose(s,state['solved'],previous)
        if s['question']:
            remember(s['question'])
        if s['question'] is None:
            print('Sınav tamamlandı!' if s['mode']=='exam' else 'Seçili levellerde çözülmemiş soru kalmadı.')
            state['session']=None
            if editor: editor.close()
        save(statepath,state)
        if s['question']:
            show(s)

    if state['session']:
        print('Kayıtlı oturuma devam ediliyor.')
        show(state['session'])
    while True:
        s=state['session']
        raw=(editor.command if editor else input)(f"{s['question'] if s else 'm2'} > ").strip()
        if not raw: continue
        cmd, _, arg=raw.partition(' ')
        cmd=cmd.lstrip('/').lower()
        if cmd=='exit':
            state['session']=None
            save(statepath,state)
            print('Oturum kapandı. Sonraki açılışta yeni mod seçebilirsin.')
            break
        if cmd=='quit':
            save(statepath,state)
            break
        if cmd in ('help','?'): print(HELP)
        elif cmd=='progress':
            for l,qs in LEVELS.items():
                print(f'Level {l}: {len(set(qs).intersection(state["solved"]))}/{len(qs)}')
        elif cmd=='api-key': configure_key(cfg,cfgpath)
        elif cmd=='model':
            for i,m in enumerate(MODELS,1): print(f'{i}. {m}'+(' *' if m==cfg.get('model',MODELS[0]) else ''))
            value=arg.strip() or input('Model numarası: ').strip()
            if value in ('1','2','3','4'):
                cfg['model']=MODELS[int(value)-1];save(cfgpath,cfg);print('Seçildi:',cfg['model'])
            else: print('Geçersiz seçim.')
        elif cmd in ('exam','practice'):
            if s: print('Açık oturum var. Yeni oturum için önce /end yaz.');continue
            setup=dict(mode='exam',levels=[1,2,3,4],repeat=True) if cmd=='exam' else practice()
            if setup:
                s=dict(setup,id=uuid.uuid4().hex,index=0,passed=0)
                state['session']=s;advance(s)
        elif cmd=='end':
            if editor: editor.close()
            state['session']=None;save(statepath,state);print('Oturum kapalı. Çözümler ve dosyalar saklanıyor.')
        elif not s: print('Önce /exam veya /practice ile başla. Komutlar: /help')
        else:
            q=s['question'];d=directory(s);p=d/filename(q)
            if cmd=='subject': show(s)
            elif cmd=='path': print(p)
            elif cmd in ('grade','grademe'):
                ok, message=grade(q,d);print(message)
                if editor and editor.root:
                    done = ok and s['mode']=='exam' and s['index']==len(s['levels'])-1
                    editor.report(ok, message + (' Sınav tamamlandı!' if done else ''))
                if ok:
                    if q not in state['solved']: state['solved'].append(q)
                    s['index']+=1;s['passed']+=1;advance(s)
                else:
                    s['last']=message;save(statepath,state);print('Aynı sorudasın. Düzenleyip yeniden /grade yaz.')
            elif cmd in ('answer','diff'):
                if editor and editor.root:
                    editor.display(cmd, arg.strip()=='long')
                    continue
                ref=solution(q,arg.strip()=='long')
                if cmd=='answer': print(ref.read_text())
                else:
                    own=p.read_text(errors='replace') if p.exists() else ''
                    print('\n'.join(difflib.unified_diff(own.splitlines(),ref.read_text().splitlines(),
                              fromfile='teslim/'+p.name,tofile='çözüm/'+ref.name,lineterm='')) or 'Kodlar aynı.')
            elif cmd=='ai':
                key=cfg.get('key') or os.environ.get('GEMINI_API_KEY')
                if not key: print('Önce /api-key ile anahtar ekle.');continue
                if not arg.strip(): print('Örnek: /ai Bu girdi için neden hata alıyorum?');continue
                code='\n'.join(f'{f.name}:\n{f.read_text(errors="replace")}' for f in sorted(d.glob('*')) if f.suffix in ('.h','.c'))
                prompt=f"Türkçe bir C eğitmeni olarak yardımcı ol.\nSubject:\n{(QUESTIONS[q]/'README.md').read_text()}\nKod:\n{code}\nSon test:\n{s['last']}\nSoru: {arg}"
                print(ask(key,cfg.get('model',MODELS[0]),prompt))
            else: print('Bilinmeyen komut. /help')


def select_milestone():
    print("42 ExamShell · Milestone seçimi\n1) M2 — Milestone 2")
    while True:
        choice = input("Seçim [1] (çıkmak için exit): ").strip().lower()
        if choice in ("", "1", "2", "m2"):
            return shell
        if choice in ("exit", "/exit", "quit", "/quit"):
            return None
        print("M2 için 1 veya M2 yaz.")


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home',type=Path,default=Path.home()/'.m2-examshell',help='ayar, ilerleme ve teslim dizini')
    parser.add_argument('--terminal', action='store_true', help='VS Code açmadan çalış')
    args=parser.parse_args()
    editor = None if args.terminal else Editor(save)
    try:
        selected = select_milestone()
        if selected:
            selected(args.home.expanduser().resolve(), editor)
    except (KeyboardInterrupt,EOFError):
        print('\nÇıkılıyor. Kaydedilen oturum sonraki açılışta devam eder.')
    finally:
        if editor: editor.close()
