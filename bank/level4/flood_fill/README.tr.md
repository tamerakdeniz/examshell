## Konu

```text
Soru adı: flood_fill
Beklenen dosyalar: *.c, *.h
İzin verilen fonksiyonlar: -
------------------------------------------------------------------------

İki boyutlu karakter dizisini char ** olarak, boyutlarını t_point size ve başlangıç noktasını t_point begin olarak alan bir fonksiyon yaz. begin noktasından başlayarak aynı karaktere sahip, yatay/dikey komşulukla bağlı bölgedeki tüm karakterleri F ile değiştir. Bölgeyi farklı karakterler veya dizi sınırları sınırlar. Çapraz komşular doldurulmaz. Aşağıdaki t_point yapısını kullan.

Fonksiyon bildirimi
void  flood_fill(char **tab, t_point size, t_point begin);
char**  area = make_area(zone, size);

Veri yapısı
typedef struct  s_point
  {
    int           x;
    int           y;
  }               t_point;

Örnekler
$> cat test.c
#include <stdlib.h>
#include <stdio.h>
#include "flood_fill.h"

char** make_area(char** zone, t_point size)
{
	char** new;

	new = malloc(sizeof(char*) * size.y);
	for (int i = 0; i < size.y; ++i)
	{
		new[i] = malloc(size.x + 1);
		for (int j = 0; j < size.x; ++j)
			new[i][j] = zone[i][j];
		new[i][size.x] = '\0';
	}

	return new;
}

int main(void)
{
	t_point size = {8, 5};
	char *zone[] = {
		"11111111",
		"10001001",
		"10010001",
		"10110001",
		"11100001",
	};

	char**  area = make_area(zone, size);
	for (int i = 0; i < size.y; ++i)
		printf("%s\n", area[i]);
	printf("\n");

	t_point begin = {7, 4};
	flood_fill(area, size, begin);
	for (int i = 0; i < size.y; ++i)
		printf("%s\n", area[i]);
	return (0);
}

$> gcc flood_fill.c test.c -o test; ./test
11111111
10001001
10010001
10110001
11100001

FFFFFFFF
F000F00F
F00F000F
F0FF000F
FFF0000F
$>
```
