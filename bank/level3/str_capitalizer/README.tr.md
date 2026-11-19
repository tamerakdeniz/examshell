## Konu

```text
Soru adı: str_capitalizer
Beklenen dosyalar: str_capitalizer.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir veya daha fazla metin al. Her metinde, her kelimenin ilk karakterini harfse büyüt, diğer harfleri küçült ve sonucu yeni satırla standart çıktıya yazdır. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Tek harflik kelime büyük yazılır. Argüman yoksa yalnızca yeni satır yazdır.

Örnekler
$> ./str_capitalizer | cat -e
$
$> ./str_capitalizer "a FiRSt LiTTlE TESt" | cat -e
A First Little Test$
$> ./str_capitalizer "__SecONd teST A LITtle BiT   Moar comPLEX" "   But... This iS not THAT COMPLEX" "     Okay, this is the last 1239809147801 but not    the least    t" | cat -e
__second Test A Little Bit   Moar Complex$
   But... This Is Not That Complex$
     Okay, This Is The Last 1239809147801 But Not    The Least    T$
$>
```
