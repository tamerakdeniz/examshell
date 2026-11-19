## Konu

```text
Soru adı: rev_wstr
Beklenen dosyalar: rev_wstr.c
İzin verilen fonksiyonlar: write, malloc, free
------------------------------------------------------------------------

Bir metindeki kelimeleri ters sırada yazdır. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Argüman sayısı 1 değilse yalnızca yeni satır yazdır. Test girdilerinde başta/sonda fazladan boşluk olmaz ve kelimeler tam bir boşlukla ayrılır.

Örnekler
$> ./rev_wstr "You hate people! But I love gatherings. Isn't it ironic?" | cat -e
ironic? it Isn't gatherings. love I But people! hate You$
$>./rev_wstr "abcdefghijklm"
abcdefghijklm
$> ./rev_wstr "Wingardium Leviosa" | cat -e
Leviosa Wingardium$
$> ./rev_wstr | cat -e
$
$>
```
