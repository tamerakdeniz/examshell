#include <unistd.h>

void putchar(char c, int i)
{
while (i--)
    {
        write(1,&c,1);
    }
}

int main(int ac, char **av)
{
    int i = 0;
    char c;

    if (ac == 2)
    {
        while (av[1][i])
        {
            c = av[1][i++];
            if (c >= 'A' && c <= 'Z')
                putchar(c, c - 'A' +1);
            else if (c > 'a' && c <= 'z')
                putchar(c, c - 'a' +1);
            else
                write(1, &c, 1);
        }
    }
    write(1, "\n", 1);
}