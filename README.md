# M2 ExamShell

42 Milestone 2 için Türkçe terminal pratiği. Soru bankasındaki 53 subject, kısa C çözümleri ve alternatif çözümler projeye dahildir. Çalıştırmak için diğer repo, Python paketi veya API anahtarı gerekmez.

## Başlat

macOS veya Linux'ta Python 3.9+, `cc` (Clang/GCC) ve IDE görünümü için VS Code gerekir. Python tarafında harici paket kurulumu gerekmez.

```sh
git clone https://github.com/tamerakdeniz/M2-Examshell.git
cd M2-Examshell
python3 examshell.py
```

Her klasörden `examshell` komutunu kullanmak için proje klasöründe çalıştır:

```sh
mkdir -p ~/.local/bin
ln -s "$PWD/examshell.py" ~/.local/bin/examshell
```

`~/.local/bin` PATH içinde değilse `export PATH="$HOME/.local/bin:$PATH"` satırını zsh için `~/.zshrc`, Bash için `~/.bashrc` dosyana ekle ve yeni terminal aç. Bağlantının çalışması için klonladığın proje klasörünü sakla.

```sh
examshell
```

Milestone menüsünde `1`, `M2` veya Enter ile Milestone 2’yi seç. Şu anda desteklenen milestone M2’dir.

İlk açılıştaki Gemini anahtarını Enter ile atlayabilirsin. Terminalde `/exam` veya `/practice` seçince VS Code oturum penceresini açar. Solda teslim dosyan, sağda subject bulunur. Kodu solda yaz ve alt durum çubuğunda **Grade** düğmesine bas. Editör teslim klasöründeki değişiklikleri kaydeder. Hatalı test **M2 · Grade** panelinde görünür. Başarılı teslimde sonraki soru aynı pencereye gelir.

**Cevabı gör** ve **Karşılaştır** düğmelerinden kısa veya uzun çözümü seçebilirsin. Karşılaştırma VS Code’un fark görünümünde açılır. **Subject** düğmesi çalışma düzenine döner. Aynı işlemler komut paletinde `M2:` ile bulunur.

ExamShell terminali oturum boyunca açık kalmalı. Uygulama kendi VS Code eklentisini bu pencere için yükler. Pencere başlığında “Extension Development Host” görebilirsin. VS Code ilk açılışta çalışma alanı güveni sorarsa oluşturulan oturum klasörünü onayla. Linux’ta `code` komutu PATH üzerinde olmalı. macOS’ta standart uygulama konumu da tanınır. Terminal düzeni için `python3 examshell.py --terminal` kullan.

## Oturumlar

- **Sınav:** 1 → 2 → 3 → 4; her levelden bir rastgele soru. Başarısız teslim aynı soruda kalır. Dört doğru teslim sınavı bitirir. Önceki sınavlarda çözülmüş sorular yeniden gelebilir. Soru seçiminde aynı leveldeki son soru, başka uygun soru varsa atlanır.
- **Pratik:** Bir veya birkaç level seç. Sıralı modda örneğin `3,1` seçimi 3 → 1 → 3 → 1 şeklinde döner. Rastgele mod her başarılı teslimden sonra uygun bir level ve o levelden bir soru seçer.
- **Pratikte tekrar kapalıysa** geçmişte sınavda veya pratikte geçtiğin sorular havuzdan çıkar. Sınav modu tamamlanmış soruları da içerir. Boş leveller atlanır; tüm havuz bitince oturum kapanır. Tekrar açıksa `/end` yazana kadar devam edebilirsin.
- **Kayıt:** Her soru için ayrı bir çalışma klasörü açılır. `exit` oturumu bitirip çıkar. Sonraki açılışta yeniden mod seçersin. `/quit` ile çıkıp aynı komutla yeniden başlattığında soruna dönersin. `/end` oturumu kapatır; kodlarını ve çözülmüş soru geçmişini saklar.

| Komut | İşlev |
|---|---|
| `/subject`, `/path` | Subject'i veya aktif C dosyasının yolunu göster |
| `/grade`, `grademe` | Teslimi derle ve çalıştır |
| `/answer`, `/answer long` | Kısa çözüm veya alternatif çözüm |
| `/diff`, `/diff long` | Teslim dosyası ile seçilen çözüm arasındaki satır farkları |
| `/progress` | Her levelde kaç farklı soru çözdüğünü gör |
| `/api-key`, `/model` | Anahtar ekle/değiştir; model seç |
| `/ai <soru>` | Örn. `/ai Son testte neden boş satır bekleniyor?` |
| `/help` | Komut listesi |

## Yerel değerlendirme

Program sorularında test argümanları ayrı ayrı aktarılır ve stdout bayt düzeyinde karşılaştırılır. Fonksiyon sorularında küçük bir C sürücüsü fonksiyonu çağırıp sonucunu okunur biçimde yazar. Örneğin `ft_strcmp` için sürücü sonucun işaretini karşılaştırır. Başarısızlıkta ilk hatalı girdi, beklenen ve alınan sonuç veya derleyici mesajı gösterilir. Satır sonları ve sekmeler çıktı karşılaştırmasında görünür. Her testin çalışma süresi 2 saniye ile sınırlıdır.

Bunlar 42'nin gizli Moulinette testleri değil, subject'lere göre yazılmış yerel davranış testleridir. Norm, yasak fonksiyon ve bellek sızıntısı denetimi yapılmaz. Teslimler yerel kullanıcı hesabında çalışır; uygulama kendi kodunu denemek içindir.

Bankanın kopyası `bank/` içinde. Kaynakta kısa çözümler `main.c` olarak verilmiş. Uygulamadaki kopyalarda testlerde bulunan bazı sorunlar (ör. yanlış fonksiyon adı, örnek main çakışması ve boş girdi davranışı) düzeltilmiştir. `hiddenp` ve `sort_in_tab` klasörlerinde teslim adı subject'e göre sırasıyla `hidenp.c` ve `sort_int_tab.c` olur.

## Gemini ve kayıtlar

Dört model kimliği: `gemini-3.5-flash-lite`, `gemini-3.8-flash`, `gemini-2.5-flash`, `gemini-3.1-flash-lite`. İstek seçilen modele gider; erişim ve kota Google hesabına ve modelin hizmet durumuna bağlıdır. Model erişilemezse `/model` ile değiştir. Yalnızca `/ai` komutu Google'a soru metnini, aktif teslimin C/header dosyalarını, son test raporunu ve yazdığın soruyu gönderir.

Ayar, ilerleme ve kodlar varsayılan olarak `~/.m2-examshell/` altında, proje dışında tutulur. Anahtar girilirse yerel `config.json` içinde şifrelenmeden, yalnızca dosya sahibinin erişebildiği izinlerle saklanır. Dosyaya kaydetmek istemezsen ilk soruyu boş bırakıp `GEMINI_API_KEY` ortam değişkenini kullan. Farklı bir profil açmak için `python3 examshell.py --home ~/.m2-ikinci-profil` çalıştır.

## Doğrulama

```sh
python3 -m unittest discover -s tests -v
```

Testler her sorunun iki çözümünü derleyip çalıştırır; hatalı teslim, oturuma dönüş, dört leveli tamamlama, pratikte seçim ve Gemini isteklerinin biçimini de kontrol eder. Testler ağ bağlantısı kullanmaz.


## Katkı

Kurulum, test, yeni soru ekleme ve pull request adımları [katkı rehberinde](CONTRIBUTING.md) bulunur. Hata bildirirken seçtiğin modu, soruyu, yeniden üretme adımlarını ve ilgili test çıktısını paylaş.

## Proje kapsamı

Bu proje 42 Milestone 2 için bağımsız bir pratik aracıdır. Soru bankası proje sahibinin M2 çalışma koleksiyonundan alınmıştır. Yerel testler subject davranışlarına göre hazırlanmıştır.


## Güncelleme

`examshell` açılışta kurulum reposunun `origin/main` dalını kontrol eder. Yeni commit varsa `/update` önerir. Milestone menüsünde veya sınav/pratik komut satırında `/update` ya da `update` yazabilirsin.

Güncelleme yalnızca temiz bir `main` dalında, fast-forward ile uygulanır. Yerel değişiklik veya ayrışmış geçmiş varsa açıklama gösterilir. Ağ erişimi yoksa uygulamayı kullanmaya devam edebilirsin. Başarılı güncellemeden sonra uygulama kapanır. VS Code’daki ExamShell penceresini kapatıp `examshell` komutunu yeniden çalıştır. Kayıtlı oturumuna M2 seçiminden sonra dönersin. Git ile klonlanmış kurulum gerekir.
