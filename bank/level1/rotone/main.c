#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    char c;
    if (ac == 2)
    {
        while (av[1][i])
        {
            c = av[1][i++];
            if ((c >= 'A' && c < 'Z') || (c >= 'a' && c < 'z'))
                c += 1;
            else if (c == 'Z')
                c = 'A';
            else if (c == 'z')
                c = 'a';
            write(1, &c, 1);
        }
    }
    write(1, "\n", 1);
}