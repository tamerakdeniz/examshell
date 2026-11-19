
#include <stdlib.h>

int get_len(long n)
{
    int len;

    len = 0;
    if (n <= 0)
        len++;
    while (n)
    {
        n = n / 10;
        len++;
    }
    return (len);
}

char *ft_itoa(int nbr)
{
    long n;
    int len;
    char *str;

    n = nbr;
    len = get_len(n);
    str = malloc(len + 1);
    if (!str)
        return NULL;
    str[len] = '\0';
    if (n == 0)
        str[0] = '0';
    if (n < 0)
    {
        str[0] = '-';
        n = -n;
    }
    while (n > 0)
    {
        str[--len] = (n % 10) + '0';
        n = n / 10; 
    }
    return (str);
}