#include <unistd.h>

int main(int argc, char **argv)
{
    int end = 0;
    int start;
    int printed = 0;

    if (argc == 2)
    {
        while (argv[1][end])
            end++;
        while (end > 0)
        {
            while (end > 0 && (argv[1][end - 1] == ' ' || argv[1][end - 1] == '\t'))
                end--;
            start = end;
            while (start > 0 && argv[1][start - 1] != ' ' && argv[1][start - 1] != '\t')
                start--;
            if (start < end)
            {
                if (printed)
                    write(1, " ", 1);
                write(1, argv[1] + start, end - start);
                printed = 1;
            }
            end = start;
        }
    }
    write(1, "\n", 1);
    return (0);
}
