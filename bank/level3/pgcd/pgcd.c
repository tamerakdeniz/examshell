
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **ag)
{
    int n1;
    int n2;
    int gcd;

    if (ac == 3)
    {
        n1 = atoi(ag[1]);
        n2 = atoi(ag[2]);
        while (n2)
        {
            gcd = n2;
            n2 = n1 % n2;
            n1 = gcd;
        }
        printf("%d", n1);
    }
    printf("\n");
    return 0;
}