
#include <unistd.h>

void putnbr(int n)
{
    long p;
    char c;

    p = n;
    if (p < 0)
    {
        p = -p;
        write (1, "-", 1);
    }
    if (p >= 10)
        putnbr(p / 10);
    c = p % 10 + '0';
    write (1, &c, 1);
}

int main(int ac, char **ag)
{
    (void)ag;

    if (ac > 1)
        putnbr(ac - 1);
    else
        write(1, "0", 1);
    write(1, "\n", 1);
    return (0);
}
