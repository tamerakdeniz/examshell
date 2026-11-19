#include <stdlib.h>
#include "ft_list.h"

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(void *, void *))
{
    t_list *removed;

    while (*begin_list)
    {
        if (cmp((*begin_list)->data, data_ref) == 0)
        {
            removed = *begin_list;
            *begin_list = removed->next;
            free(removed);
        }
        else
            begin_list = &(*begin_list)->next;
    }
}
