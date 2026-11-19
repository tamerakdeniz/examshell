
#include <unistd.h>

int main(int ac, char **ag)
{
    int i;
    int j;

    if (ac > 1)
    {
        i = 1;
        while (i < ac)
        {   
            j = 0;
            while (ag[i][j])
            {
                if (ag[i][j] >= 'A' && ag[i][j] <= 'Z')
                    ag[i][j] += 32;
                if ((ag[i][j] >= 'a' && ag[i][j] <= 'z') && (ag[i][j + 1] == ' ' || ag[i][j + 1] == '\t' || ag[i][j + 1] == '\0'))
                    ag[i][j] -= 32;
                write(1, &ag[i][j], 1);
                j++;
            }
            write(1, "\n", 1);
            i++;
        }
    }
    else
        write(1, "\n", 1);
    return 0;
}
    
