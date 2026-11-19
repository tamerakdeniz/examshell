## Konu

```text
Soru adı: last_word
Beklenen dosyalar: last_word.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir metnin son kelimesini ve ardından yeni satır yazdır. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Argüman sayısı 1 değilse ya da kelime yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./last_word "FOR PONY" | cat -e
PONY$
$> ./last_word "this        ...       is sparta, then again, maybe    not" | cat -e
not$
$> ./last_word "   " | cat -e
$
$> ./last_word "a" "b" | cat -e
$
$> ./last_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>
```
