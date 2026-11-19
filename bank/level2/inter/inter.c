
#include <unistd.h>

int seen(char *str, int pos)
{
    int i;
    i = 0;
    while (i < pos)
    {
        if (str[i] == str[pos])
            return(1);
        i++;
    }
    return 0;
}

int main(int ac, char **ag)
{
    if (ac == 3)
    {
        int i;
        int j;
        i = 0;
        while (ag[1][i])
        {
            j = 0;
            while (ag[2][j])
            {
                if (!seen(ag[1], i))
                {
                    if (ag[1][i] == ag[2][j])
                    {
                        write(1, &ag[1][i], 1);
                        break;
                    }
                }
                j++;
            }
            i++;
        }
    }
    write(1, "\n", 1);
    return 0;
}