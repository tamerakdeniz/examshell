## Konu

```text
Soru adı: ft_list_foreach
Beklenen dosyalar: ft_list_foreach.c, ft_list.h
İzin verilen fonksiyonlar:
------------------------------------------------------------------------

Bir liste ve fonksiyon işaretçisi al. Fonksiyonu listedeki her elemanın data alanına uygula: (*f)(list_ptr->data). Aşağıdaki yapıyı kullan ve ft_list.h adıyla teslim et.

Fonksiyon bildirimi
void    ft_list_foreach(t_list *begin_list, void (*f)(void *));

Veri yapısı
typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;
```
