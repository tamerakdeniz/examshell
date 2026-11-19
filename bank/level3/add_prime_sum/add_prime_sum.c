
#include <unistd.h>

int ft_atoi(char *s)
{
    int nb;

    nb = 0;
    while (*s >= '0' && *s <= '9')
    {
        nb = nb * 10 + (*s - '0');
        s++;
    }
    return (nb);
}

void putnbr(int n)
{
    char c;

    if (n > 9)
        putnbr(n / 10);
    c = n % 10 + '0';
    write(1, &c, 1);
}
int is_prime(int n)
{
    int i;

    i = 2;
    if (n <= 1)
        return 0;
    while (i * i <= n)
    {
        if (n % i == 0)
            return 0;
        i++;
    }
    return (1);
}

int main(int ac, char **ag)
{
    int nb;
    int sum;

    if (ac == 2 && ag[1][0] >= '0' && ag[1][0] <= '9')
    {
        nb = ft_atoi(ag[1]);
        sum = 0;
        while (nb > 0)
        {
            if (is_prime(nb))
                sum = sum + nb;
            nb--;
        }
        putnbr(sum);
    }
    else
        write(1, "0", 1);
    write (1, "\n", 1);
    return 0;
}