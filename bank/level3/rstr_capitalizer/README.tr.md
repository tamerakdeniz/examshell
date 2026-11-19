## Konu

```text
Soru adı: rstr_capitalizer
Beklenen dosyalar: rstr_capitalizer.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir veya daha fazla metin al. Her metinde, her kelimenin son karakterini harfse büyüt, diğer harfleri küçült ve sonucu yeni satırla yazdır. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Tek harflik kelime büyük yazılır. Harfler [a-zA-Z] kümesindedir. Argüman yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./rstr_capitalizer | cat -e
$
$> ./rstr_capitalizer "a FiRSt LiTTlE TESt" | cat -e
A firsT littlE tesT$
$> ./rstr_capitalizer "SecONd teST A LITtle BiT   Moar comPLEX" "   But... This iS not THAT COMPLEX" "     Okay, this is the last 1239809147801 but not    the least    t" | cat -e
seconD tesT A littlE biT   moaR compleX$
   but... thiS iS noT thaT compleX$
     okay, thiS iS thE lasT 1239809147801 buT noT    thE leasT    T$
$>
```
