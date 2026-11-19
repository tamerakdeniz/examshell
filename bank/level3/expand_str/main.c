#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    int printed = 0;

    if (argc == 2)
    {
        while (argv[1][i])
        {
            while (argv[1][i] == ' ' || argv[1][i] == '\t')
                i++;
            if (argv[1][i] && printed)
                write(1, "   ", 3);
            while (argv[1][i] && argv[1][i] != ' ' && argv[1][i] != '\t')
            {
                write(1, &argv[1][i++], 1);
                printed = 1;
            }
        }
    }
    write(1, "\n", 1);
    return (0);
}
