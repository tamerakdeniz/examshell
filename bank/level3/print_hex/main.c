#include <unistd.h>

static void print_hex(unsigned int n)
{
    if (n >= 16)
        print_hex(n / 16);
    write(1, &"0123456789abcdef"[n % 16], 1);
}

int main(int argc, char **argv)
{
    unsigned int n = 0;
    int i = 0;

    if (argc == 2)
    {
        while (argv[1][i] >= '0' && argv[1][i] <= '9')
            n = n * 10 + argv[1][i++] - '0';
        print_hex(n);
    }
    write(1, "\n", 1);
    return (0);
}
