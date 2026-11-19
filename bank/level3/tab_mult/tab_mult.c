
#include <unistd.h>

int ft_atoi(char *str)
{
    int nb;
    int sign;

    nb = 0;
    sign = 1;
    while(*str == 32 || (*str >= 9 && *str <= 13))
        str++;
    if (*str == '+' || *str == '-')
    {
        if (*str == '-')
            sign = -1 * sign;
        str++;
    }
    while (*str >= '0' && *str <= '9')
    {
        nb = nb * 10 + (*str - '0');
        str++;
    }
    return (nb * sign);
}

void putnbr(int nb)
{
    long p;
    char c;

    p = nb;
    if (p < 0)
    {
        p = -p;
        write(1, "-", 1);
    }
    if (p >= 10)
        putnbr(p / 10);
    c = p % 10 + '0';
    write(1, &c, 1);
}

int main(int ac, char **ag)
{
    int i;
    int nb;

    if (ac == 2)
    {
        i = 1;
        nb = ft_atoi(ag[1]);
        while (i <= 9)
        {
            putnbr(i);
            write(1, " x ", 3);
            putnbr(nb);
            write(1, " = ", 3);
            putnbr(i * nb);
            write(1, "\n", 1);
            i++;
        }
    }
    else
        write(1, "\n", 1);
    return (0);
}