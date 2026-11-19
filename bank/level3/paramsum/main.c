#include <unistd.h>

static void putnbr(unsigned long n)
{
    if (n >= 10)
        putnbr(n / 10);
    write(1,&"0123456789"[n % 10], 1);
    
}

int main(int ac, char **av)
{
    (void)av;
    putnbr(ac - 1);
    write(1, "\n", 1);
}