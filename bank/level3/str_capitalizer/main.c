#include <unistd.h>

int main(int argc, char **argv)
{
    int arg = 1;
    int i;
    char *str;

    if (argc == 1)
        write(1, "\n", 1);
    while (arg < argc)
    {
        str = argv[arg++];
        i = 0;
        while (str[i])
        {
            if (str[i] >= 'A' && str[i] <= 'Z')
                str[i] += 32;
            if (str[i] >= 'a' && str[i] <= 'z' && (i == 0 || str[i - 1] == ' ' || str[i - 1] == '\t'))
                str[i] -= 32;
            write(1, &str[i++], 1);
        }
        write(1, "\n", 1);
    }
    return (0);
}
