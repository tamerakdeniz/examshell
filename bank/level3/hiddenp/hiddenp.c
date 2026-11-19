
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int j;

    if (ac == 3)
    {
        i = 0;
        j = 0;
        while (ag[2][j])
        {
            if (ag[1][i] == ag[2][j])
                i++;
            j++;
        }
        if (ag[1][i] == '\0')
            write(1, "1", 1);
        else
            write(1, "0", 1);
    }
    write (1, "\n", 1);
    return 0;
}