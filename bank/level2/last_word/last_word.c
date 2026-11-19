
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int end;

    if (ac == 2)
    {
        i = 0;
        while (ag[1][i])
            i++;
        i--;
        while (i >= 0 && (ag[1][i] == ' ' || ag[1][i] == '\t'))
            i--;
        end = i;
        while (i >= 0 && ag[1][i] != ' ' && ag[1][i] != '\t')
            i--;
        i++;
        while (i <=end)
        {
            write (1, &ag[1][i], 1);
            i++;
        }
    }
    write (1, "\n", 1);
    return (0);
}