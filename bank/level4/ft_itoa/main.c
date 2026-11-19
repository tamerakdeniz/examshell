#include <stdlib.h>

char *ft_itoa(int nbr)
{
    long n = nbr;
    long copy = n;
    int len = 1;
    char *str;

    if (n < 0)
    {
        n = -n;
        len++;
    }
    while (copy / 10)
    {
        len++;
        copy /= 10;
    }
    str = malloc(len + 1);
    if (!str)
        return (NULL);
    str[len] = '\0';
    while (len > 0)
    {
        str[--len] = n % 10 + '0';
        n /= 10;
    }
    if (nbr < 0)
        str[0] = '-';
    return (str);
}
