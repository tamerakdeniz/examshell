#include <unistd.h>

int main(int argc, char **argv)
{
    char *str;
    char *first;
    int len = 0;

    if (argc > 1)
    {
        str = argv[1];
        while (*str == ' ' || *str == '\t')
            str++;
        first = str;
        while (*str && *str != ' ' && *str != '\t')
        {
            len++;
            str++;
        }
        while (*str)
        {
            while (*str == ' ' || *str == '\t')
                str++;
            if (*str)
            {
                while (*str && *str != ' ' && *str != '\t')
                    write(1, str++, 1);
                write(1, " ", 1);
            }
        }
        write(1, first, len);
    }
    write(1, "\n", 1);
    return (0);
}
