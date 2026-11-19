#include "list.h"

t_list *sort_list(t_list *lst, int (*cmp)(int, int))
{
    t_list *node = lst;
    int temp;

    while (node && node->next)
    {
        if (!cmp(node->data, node->next->data))
        {
            temp = node->data;
            node->data = node->next->data;
            node->next->data = temp;
            node = lst;
        }
        else
            node = node->next;
    }
    return (lst);
}
