## Konu

```text
Soru adı: repeat_alpha
Beklenen dosyalar: repeat_alpha.c
İzin verilen fonksiyonlar: write
------------------------------------------------------------------------

Bir metindeki her harfi alfabedeki sıra numarası kadar tekrar ederek yazdır. Örneğin a → a, b → bb, e → eeeee. Büyük/küçük harf durumunu koru. Diğer karakterler aynı kalır. Çıktı yeni satırla biter. Argüman sayısı 1 değilse yalnızca yeni satır yazdır.

Örnekler
$>./repeat_alpha "abc"
abbccc
$>./repeat_alpha "Alex." | cat -e
Alllllllllllleeeeexxxxxxxxxxxxxxxxxxxxxxxx.$
$>./repeat_alpha 'abacadaba 42!' | cat -e
abbacccaddddabba 42!$
$>./repeat_alpha | cat -e
$
$>
$>./repeat_alpha "" | cat -e
$
$>
```
