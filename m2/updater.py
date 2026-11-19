"""Fast-forward updates from the installation's origin/main."""
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent


class UpdateError(Exception):
    pass


class Updated(Exception):
    """Exit the running version after installing a new version."""


def git(root, *args):
    try:
        result = subprocess.run(
            ['git', '-C', str(root), *args], capture_output=True, text=True,
            timeout=15, env=dict(os.environ, GIT_TERMINAL_PROMPT='0'),
        )
    except FileNotFoundError as error:
        raise UpdateError('Git bulunamadı.') from error
    except subprocess.TimeoutExpired as error:
        raise UpdateError('Güncelleme kontrolü zaman aşımına uğradı. Daha sonra /update deneyebilirsin.') from error
    if result.returncode:
        raise UpdateError('Git işlemi tamamlanamadı. Ağ bağlantısını ve origin/main erişimini kontrol et.')
    return result.stdout.strip()


def check(root=ROOT):
    if not (root / '.git').exists():
        raise UpdateError('Bu kurulum Git ile klonlanmamış. Güncelleme için README’deki git clone adımlarını kullan.')
    git(root, 'fetch', '--quiet', 'origin', 'refs/heads/main')
    target = git(root, 'rev-parse', 'FETCH_HEAD')
    behind = int(git(root, 'rev-list', '--count', f'HEAD..{target}'))
    return target, behind


def announce():
    try:
        _, behind = check()
        if behind:
            print(f'Yeni sürüm var ({behind} commit). Güncellemek için /update yaz.')
    except UpdateError as error:
        print(f'Güncelleme kontrolü: {error}')


def update(root=ROOT):
    try:
        if git(root, 'status', '--porcelain', '--untracked-files=all'):
            raise UpdateError('Kurulum klasöründe yerel değişiklikler var. Değişikliklerini commit edip veya saklayıp /update komutunu yeniden çalıştır.')
        if git(root, 'symbolic-ref', '--short', 'HEAD') != 'main':
            raise UpdateError('Güncelleme main dalında yapılabilir. Önce main dalına geç.')
        target, behind = check(root)
        if not behind:
            print('ExamShell güncel.')
            return
        if int(git(root, 'rev-list', '--count', f'{target}..HEAD')):
            raise UpdateError('Yerel ve uzak geçmiş ayrışmış. Git üzerinden birleştirdikten sonra tekrar dene.')
        git(root, 'merge', '--ff-only', target)
    except UpdateError as error:
        print(f'Güncelleme uygulanamadı: {error}')
        return
    print('Güncelleme tamamlandı. Açık oturumun kayıtlı. VS Code’daki ExamShell penceresini kapatıp examshell komutunu yeniden çalıştır.')
    raise Updated()
