
#include <stdlib.h>

int     *ft_rrange(int start, int end)
{
    int *res;
    int i;
    int len;

    if (start <= end)
        len = end - start + 1;
    else
        len = (start - end) + 1;
    res = (int *)malloc(sizeof(int) * len);
    if (!res)
        return NULL;
    i = 0;
    if(start <= end)
    {
        while(i < len)
        {
            res[i] = end;
            end--;
            i++;
        }
    }
    else
    {
        while (i < len)
        {
            res[i] = end;
            end++;
            i++;
        }
    }
    return(res);
}
