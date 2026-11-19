
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;

    if(ac == 2)
    {
        i = 0;
        while(ag[1][i])
        {
            if (ag[1][i] >= 'A' && ag[1][i] <= 'Z')
            {
                write(1, "_", 1);
                ag[1][i] += 32;
            }
            write(1, &ag[1][i], 1);
            i++;
        }
    }
    write (1, "\n", 1);
    return (0);
}