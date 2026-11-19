## Konu

```text
Soru adı: expand_str
Beklenen dosyalar: expand_str.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir metni kelimeler arasında tam üç boşluk olacak şekilde yazdır. Başta ve sonda boşluk veya sekme bulunmamalıdır. Sonuna yeni satır ekle. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Argüman sayısı 1 değilse ya da kelime yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./expand_str "See? It's easy to print the same thing" | cat -e
See?   It's   easy   to   print   the   same   thing$
$> ./expand_str " this        time it      will     be    more complex  " | cat -e
this   time   it   will   be   more   complex$
$> ./expand_str "No S*** Sherlock..." "nAw S*** ShErLaWQ..." | cat -e
$
$> ./expand_str "" | cat -e
$
$>
```
