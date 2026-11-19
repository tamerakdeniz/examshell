## Konu

```text
Soru adı: ft_list_remove_if
Beklenen dosyalar: ft_list_remove_if.c
İzin verilen fonksiyonlar: free
------------------------------------------------------------------------

data alanı referans veriyle eşit olan tüm elemanları bağlı listeden kaldıran ft_list_remove_if fonksiyonunu yaz. cmp iki void* alır ve eşitlerse 0 döndürür. Aşağıdaki yapıyı içeren ft_list.h dosyasını kullan.

Fonksiyon bildirimi
void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)());

Veri yapısı
typedef struct      s_list
{
    struct s_list   *next;
    void            *data;
}                   t_list;
```
