#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int n;
    int factor = 2;

    if (argc == 2)
    {
        n = atoi(argv[1]);
        while (factor <= n / factor)
        {
            if (n % factor == 0)
            {
                printf("%d*", factor);
                n /= factor;
            }
            else
                factor++;
        }
        printf("%d", n);
    }
    printf("\n");
}
