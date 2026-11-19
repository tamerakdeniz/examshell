#include <stdlib.h>

char    *ft_strdup(char *src)
{
    char *temp;
    int i = 0;
    int len = 0;

    while (src[len++]);
    temp = malloc(len);
    if (!temp)
        return (NULL);
    while (src[i])
    {
        temp[i] = src[i];
        i++;
    }
    temp[i] = '\0';
    return (temp);
}