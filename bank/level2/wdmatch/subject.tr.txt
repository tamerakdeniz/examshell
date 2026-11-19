## Konu

```text
Soru adı: wdmatch
Beklenen dosyalar: wdmatch.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

İki metin al. İlk metnin, ikinci metindeki karakterler sıraları korunarak seçilerek oluşturulup oluşturulamayacağını kontrol et. Oluşturulabiliyorsa ilk metni ve yeni satır yazdır. Aksi durumda yalnızca yeni satır yazdır. Argüman sayısı 2 değilse yalnızca yeni satır yazdır.

Örnekler
$>./wdmatch "faya" "fgvvfdxcacpolhyghbreda" | cat -e
faya$
$>./wdmatch "faya" "fgvvfdxcacpolhyghbred" | cat -e
$
$>./wdmatch "quarante deux" "qfqfsudf arzgsayns tsregfdgs sjytdekuoixq " | cat -e
quarante deux$
$>./wdmatch "error" rrerrrfiiljdfxjyuifrrvcoojh | cat -e
$
$>./wdmatch | cat -e
$
```
