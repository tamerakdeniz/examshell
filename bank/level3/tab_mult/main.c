#include <unistd.h>

static void putnbr(unsigned long n)
{
    if (n >= 10)
        putnbr(n / 10);
    write(1, &"0123456789"[n % 10], 1);
}

int main(int argc, char **argv)
{
    int n = 0;
    int i = 0;
    int row = 1;

    if (argc == 2)
    {
        while (argv[1][i] >= '0' && argv[1][i] <= '9')
            n = n * 10 + argv[1][i++] - '0';
        while (row <= 9)
        {
            putnbr(row);
            write(1, " x ", 3);
            putnbr(n);
            write(1, " = ", 3);
            putnbr(n * row++);
            write(1, "\n", 1);
        }
    }
    else
        write(1, "\n", 1);
}
