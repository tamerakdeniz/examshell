
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int flag;

    if (ac == 2)
    {
        i = 0;
        flag = 0;
        while (ag[1][i] == ' ' || ag[1][i] == '\t')
            i++;
        while(ag[1][i])
        {
            if (ag[1][i] == ' ' || ag[1][i] == '\t')
                flag = 1;
            if (ag[1][i] != ' ' && ag[1][i] != '\t')
            {
                if (flag)
                    write(1, "   ", 3);
                flag = 0;
                write (1, &ag[1][i], 1);
            }
            i++;
        }
    }
    write (1, "\n", 1);
    return 0;
}