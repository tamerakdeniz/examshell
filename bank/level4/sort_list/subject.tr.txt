## Konu

```text
Soru adı: sort_list
Beklenen dosyalar: sort_list.c
İzin verilen fonksiyonlar:
------------------------------------------------------------------------

Bağlı listeyi cmp fonksiyonunun belirlediği sıraya göre sırala ve sıralı listenin ilk elemanına işaretçiyi döndür. Tekrarlanan değerleri koru. Girdiler her zaman tutarlıdır. Sağlanan list.h içindeki t_list türünü kullan ve dosyayı #include "list.h" ile dahil et; bu header dosyasını teslim etme, değerlendirmede sağlanan sürüm kullanılır. cmp, a ve b doğru sıradaysa sıfırdan farklı, değilse 0 döndürür. Örneğin aşağıdaki karşılaştırıcı artan sırayı belirtir:

int ascending(int a, int b)
{
    return (a <= b);
}

Fonksiyon bildirimi
t_list	*sort_list(t_list* lst, int (*cmp)(int, int));
```
