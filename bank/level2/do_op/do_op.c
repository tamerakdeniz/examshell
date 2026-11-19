
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **ag)
{
    int i;
    int j;

    
    if (ac == 4)
    {
        i = atoi(ag[1]);
        j = atoi(ag[3]);
        if (ag[2][0] == '+')
            printf("%i", i + j);
        else if(ag[2][0] == '-')
            printf("%i", i - j);
        else if(ag[2][0] == '*')
            printf("%i", i * j);
        else if(ag[2][0] == '/')
            printf("%i", i / j);
        else if (ag[2][0] == '%')
            printf("%i", i % j);
    }
    printf("\n");
    return 0;
}