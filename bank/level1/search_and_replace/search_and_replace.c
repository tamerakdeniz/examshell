
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;

    if (ac == 4 && ag[2][0] && !ag[2][1] && ag[3][0] && !ag[3][1])
    {
        i = 0;
        while (ag[1][i])
        {
            if (ag[1][i] == ag[2][0])
                ag[1][i] = ag[3][0];
            write(1, &ag[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
    return(0);
}
