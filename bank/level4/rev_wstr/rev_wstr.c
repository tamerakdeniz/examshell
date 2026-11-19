
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int start;
    int end;

    i = 0;
    if (ac == 2)
    {
        while(ag[1][i] != '\0')
            i++;
        i--;
        while (i >= 0)
        {
            while (i >= 0 && (ag[1][i] == '\0' || ag[1][i] == ' ' || ag[1][i] == '\t'))
                i--;
            end = i;
            while (i >= 0 && (ag[1][i] && ag[1][i] != ' ' && ag[1][i] != '\t'))
                i--;
            start = i + 1;
            while (start <= end)
            {
                write(1, &ag[1][start], 1);
                start++;
            }
            if (i >= 0)
                write(1, " ", 1);
        }
    }
    write(1, "\n", 1);
    return (0);
}