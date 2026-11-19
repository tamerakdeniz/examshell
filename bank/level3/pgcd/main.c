#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int a;
    int b;
    int remainder;

    if (argc == 3)
    {
        a = atoi(argv[1]);
        b = atoi(argv[2]);
        while (b)
        {
            remainder = a % b;
            a = b;
            b = remainder;
        }
        printf("%d", a);
    }
    printf("\n");
    return (0);
}
