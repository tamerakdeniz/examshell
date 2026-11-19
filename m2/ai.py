"""Optional Gemini REST client, using only the standard library."""
import json
import urllib.error
import urllib.request

MODELS = ('gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash', 'gemini-3.1-flash-lite')


def ask(key, model, prompt):
    if model not in MODELS:
        return 'Geçersiz model. /model ile seçim yap.'
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
    body = {'contents': [{'parts': [{'text': prompt}]}]}
    request = urllib.request.Request(url, data=json.dumps(body).encode(),
                                     headers={'Content-Type':'application/json','x-goog-api-key':key})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            result = json.load(response)
        parts = (result.get('candidates') or [{}])[0].get('content',{}).get('parts',[])
        return '\n'.join(p['text'] for p in parts if 'text' in p and not p.get('thought')) or 'Model metin döndürmedi.'
    except urllib.error.HTTPError as error:
        hint = {400:'Anahtarı ve isteği kontrol et.',403:'API anahtarını ve erişim izinlerini kontrol et.',
                404:'Bu model anahtarın için kullanılamıyor. /model ile başka birini seç.',
                429:'Kota veya istek sınırı doldu.'}
        return f'Gemini HTTP {error.code}: '+hint.get(error.code,'Servis isteği tamamlayamadı.')
    except (OSError, ValueError):
        return 'Gemini yanıtı alınamadı. Bağlantını kontrol et.'
