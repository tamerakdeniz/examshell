## Konu

```text
Soru adı: do_op
Beklenen dosyalar: *.c, *.h
İzin verilen fonksiyonlar: atoi, printf, write
------------------------------------------------------------------------

Üç metin argümanı al. Birinci ve üçüncü argüman int aralığındaki işaretli onluk tamsayılardır. İkinci argüman + - * / % işleçlerinden biridir. İşlem sonucunu yeni satırla yazdır. Argüman sayısı 3 değilse yalnızca yeni satır yazdır. Girdilerde hata veya fazladan karakter bulunmaz. Negatif sayılarda başta tek bir eksi işareti vardır. Sonuç int aralığına sığar.

Örnekler
$> ./do_op "123" "*" 456 | cat -e
56088$
$> ./do_op "9828" "/" 234 | cat -e
42$
$> ./do_op "1" "+" "-43" | cat -e
-42$
$> ./do_op | cat -e
$
```
