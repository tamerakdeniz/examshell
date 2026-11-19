# Katkı rehberi

M2 ExamShell, Python standart kütüphanesiyle çalışan bir sınav ve pratik uygulaması ve JavaScript ile yazılmış bir VS Code eklentisinden oluşur.

## Geliştirme ortamı

Repoyu klonlayıp Python 3.9+, Clang/GCC ve VS Code kur. JavaScript sözdizimi kontrolü için Node.js kullanılır. Terminal akışını ayrı bir test profiliyle çalıştırabilirsin.

```sh
python3 examshell.py --terminal --home /tmp/m2-development
python3 -m unittest discover -s tests -v
node --check vscode/extension.js
```

IDE akışı için `--terminal` seçeneğini kaldır. Test profilinde ilk açılışta API anahtarını boş bırakabilirsin.

## Dosya düzeni

| Yol | İçerik |
|---|---|
| `examshell.py` | Milestone seçimi, oturum, pratik ve komutlar |
| `m2/grader.py` | C derleme, çalıştırma ve sonuç karşılaştırma |
| `m2/cases.py` | Program testleri ve fonksiyon sürücüleri |
| `m2/editor.py` | Python ile VS Code arasındaki dosya tabanlı iletişim |
| `m2/ai.py` | Gemini istemcisi |
| `vscode/` | VS Code eklentisi ve komutları |
| `bank/level*/` | Subject, kısa çözüm, alternatif çözüm ve header dosyaları |
| `tests/` | Python regresyon testleri |

## Hata bildirimi

Issue içinde işletim sistemini, Python sürümünü, terminal veya IDE modunu, sorunun adını ve hatayı üreten adımları belirt. Beklediğin davranışı ve gözlemlediğin sonucu ekle. Test hatasında ilgili girdiyi ve çıktıyı paylaş. API anahtarlarını ve kişisel profil dosyalarını rapora ekleme.

## Değişiklik gönderme

1. Fork üzerinde değişiklik için bir branch oluştur.
2. Commitleri soru bankası, uygulama davranışı, IDE veya dokümantasyon gibi anlamlı kapsamlarla ayır.
3. Değişen davranışı mevcut testlerle doğrula. Bir hata düzeltiyorsan onu yeniden üreten bir regresyon testi ekle.
4. Pull request açıklamasında problemi, değişen davranışı ve yaptığın doğrulamayı yaz.

IDE değişikliklerinde soldaki teslim ile sağdaki subject eşleşmesini, Grade ile kaydetmeyi, hatalı teslimden sonra aynı soruda kalmayı ve başarılı teslimle sonraki soruya geçmeyi dene. `exit` sonrası yeni oturumu ve `/quit` sonrası aynı soruya dönüşü kontrol et.

## Soru ekleme

Soruyu uygun `bank/levelN/soru_adi/` klasörüne ekle. Subject'i `README.md`, kısa çözümü `main.c`, alternatif çözümü `soru_adi.c` olarak yerleştir. Gereken header dosyalarını aynı klasöre koy. Teslim dosyası klasör adından farklıysa `m2/grader.py` içindeki dosya eşlemesini güncelle.

Program sorusu için argüman ve beklenen çıktı çiftleri, fonksiyon sorusu için C sürücüsü ve beklenen sonuçlar ekle. İki çözümü de test et. Soru sayısı değişirse kullanıcıya gösterilen toplamı ve belgeleri güncelle. Beklenen çıktıları subject'ten türet.

Yeni milestone eklerken onun soru bankasını, değerlendiricisini ve kayıt düzenini tanımla. Mevcut M2 ilerleme dosyalarıyla uyumluluğu koru.

## README güncellemeleri

README, projeyi ilk kez klonlayan bir kullanıcının kurup çalıştırabileceği adımları içermeli. Komut, kurulum gereksinimi veya oturum davranışı değiştiğinde ilgili bölümü güncelle. Tamamlanan özelliklerle henüz doğrulanmamış davranışları açıkça belirt.
