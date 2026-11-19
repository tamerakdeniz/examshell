#include <unistd.h>

static void putnbr(unsigned long n)
{
    char digit = n % 10 + '0';

    if (n >= 10)
        putnbr(n / 10);
    write(1, &digit, 1);
}

static int is_prime(long n)
{
    long divisor = 2;

    while (divisor <= n / divisor)
    {
        if (n % divisor == 0)
            return (0);
        divisor++;
    }
    return (n >= 2);
}

int main(int argc, char **argv)
{
    long n = 0;
    long candidate = 2;
    unsigned long sum = 0;
    int i = 0;

    if (argc == 2)
    {
        if (argv[1][i] == '+')
            i++;
        while (argv[1][i] >= '0' && argv[1][i] <= '9')
            n = n * 10 + argv[1][i++] - '0';
        if (argv[1][i])
            n = 0;
        while (candidate <= n)
        {
            if (is_prime(candidate))
                sum += candidate;
            candidate++;
        }
    }
    putnbr(sum);
    write(1, "\n", 1);
    return (0);
}
