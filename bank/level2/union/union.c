
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
    return (0);
}
int main(int ac, char **ag)
{
    int i;
    int j;
    int k;

    if (ac == 3)
    {
        i = 0;
        j = 0;
        while (ag[1][i])
            i++;
        while (ag[2][j])
        {
            ag[1][i] = ag[2][j];
            i++;
            j++;
        }
        i--;
        k = 0;
        while (k <= i)
        {
            if (!seen(ag[1], k))
                write (1, &ag[1][k], 1);
            k++;
        }
    }
    write(1, "\n", 1);
    return (0);
}