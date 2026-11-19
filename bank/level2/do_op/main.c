#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    int i;
    int j;
    char c;
    if (ac == 4)
    {
        c = av[2][0];
        i = atoi(av[1]);
        j = atoi(av[3]);
        if (c == '+')
            printf("%i", i + j);
        else if (c == '-')
            printf("%i", i - j);
        else if (c == '*')
            printf("%i", i * j);
        else if (c == '/')
            printf("%i", i / j);
        else if (c == '%')
            printf("%i", i % j);
    }
    printf("\n"); 
}