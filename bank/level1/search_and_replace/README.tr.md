## Konu

```text
Soru adı: search_and_replace
Beklenen dosyalar: search_and_replace.c
İzin verilen fonksiyonlar: write, exit
------------------------------------------------------------------------

Üç argüman alan bir program yaz. İlk argüman metindir. İkinci argümandaki harfin tüm örneklerini üçüncü argümandaki harfle değiştir. Aranan harf bulunmazsa metni olduğu gibi yazdır. Sonuna yeni satır ekle. Argüman sayısı 3 değilse veya ikinci/üçüncü argüman tek karakter değilse yalnızca yeni satır yazdır.

Örnekler
$>./search_and_replace "Papache est un sabre" "a" "o"
Popoche est un sobre
$>./search_and_replace "zaz" "art" "zul" | cat -e
$
$>./search_and_replace "zaz" "r" "u" | cat -e
zaz$
$>./search_and_replace "jacob" "a" "b" "c" "e" | cat -e
$
$>./search_and_replace "ZoZ eT Dovid oiME le METol." "o" "a" | cat -e
ZaZ eT David aiME le METal.$
$>./search_and_replace "wNcOre Un ExEmPle Pas Facilw a Ecrirw " "w" "e" | cat -e
eNcOre Un ExEmPle Pas Facile a Ecrire $
```
