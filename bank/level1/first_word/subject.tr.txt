## Konu

```text
Soru adı: first_word
Beklenen dosyalar: first_word.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir metin alıp ilk kelimesini ve ardından yeni satır yazdıran bir program yaz. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Argüman sayısı 1 değilse ya da kelime yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./first_word "FOR PONY" | cat -e
FOR$
$> ./first_word "this        ...    is sparta, then again, maybe    not" | cat -e
this$
$> ./first_word "   " | cat -e
$
$> ./first_word "a" "b" | cat -e
$
$> ./first_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>
```
