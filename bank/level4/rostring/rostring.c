
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int start;
    int end;
    int flag;

    if (ac > 1)
    {
        i = 0;
        flag = 0;
        while (ag[1][i] && (ag[1][i] == ' ' || ag[1][i] == '\t'))
            i++;
        start = i;
        while (ag[1][i] && !(ag[1][i] == ' ' || ag[1][i] == '\t'))
            i++;
        end = i;
        while(ag[1][i])
        {
            while (ag[1][i] && (ag[1][i] == ' ' || ag[1][i] == '\t'))
                i++; 
            if (ag[1][i] && flag)
                write(1, " ", 1);
            while (ag[1][i] && !(ag[1][i] == ' ' || ag[1][i] == '\t'))
            {
                write(1, &ag[1][i], 1);
                i++;
                flag = 1;
            }
        }
        if (flag)
            write (1, " ", 1);
        while (start < end)
        {
            write (1, &ag[1][start], 1);
            start++;
        }
    }
    write(1, "\n", 1);
    return 0;
}