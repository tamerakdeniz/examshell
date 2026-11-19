## Konu

```text
Soru adı: epur_str
Beklenen dosyalar: epur_str.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir metni kelimeler arasında tam bir boşluk olacak şekilde yazdır. Başta ve sonda boşluk veya sekme bulunmamalıdır. Sonuna yeni satır ekle. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Argüman sayısı 1 değilse ya da kelime yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./epur_str "See? It's easy to print the same thing" | cat -e
See? It's easy to print the same thing$
$> ./epur_str " this        time it      will     be    more complex  . " | cat -e
this time it will be more complex .$
$> ./epur_str "No S*** Sherlock..." "nAw S*** ShErLaWQ..." | cat -e
$
$> ./epur_str "" | cat -e
$
$>
```
