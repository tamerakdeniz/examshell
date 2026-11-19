## Konu

```text
Soru adı: rostring
Beklenen dosyalar: rostring.c
İzin verilen fonksiyonlar: write, malloc, free
------------------------------------------------------------------------

Bir metni kelimeler açısından bir adım sola döndürerek yazdır: ilk kelime sona gider, diğerleri sıralarını korur. Kelime, boşluk/sekme veya metnin başı/sonuyla sınırlanır. Çıktıda kelimeler arasında tek boşluk bulunur ve çıktı yeni satırla biter. Argüman yoksa yalnızca yeni satır yazdır.

Örnekler
$>./rostring "abc   " | cat -e
abc$
$>
$>./rostring "Que la      lumiere soit et la lumiere fut"
la lumiere soit et la lumiere fut Que
$>
$>./rostring "     AkjhZ zLKIJz , 23y"
zLKIJz , 23y AkjhZ
$>
$>./rostring "first" "2" "11000000"
first
$>
$>./rostring | cat -e
$
$>
```
