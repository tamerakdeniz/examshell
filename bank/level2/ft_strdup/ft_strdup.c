
#include <stdlib.h>

char *ft_strdup(char *src)
{
    char *dup;
    int len = 0;
    int i = 0;

    while(src[len++]);
    dup = malloc(sizeof(char)* len+ 1);
    if (!dup)
        return NULL;
    while (src[i])
    {
        dup[i] = src[i];
        i++;
    }
    dup[i] = '\0';
    return dup;
}
