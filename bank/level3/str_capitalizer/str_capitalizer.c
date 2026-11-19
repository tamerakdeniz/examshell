#include <unistd.h>


char to_upper(char c)
{
    if (c >= 'a' && c <= 'z')
        c = c - 32;
    return (c);
}
char to_lower(char c)
{
    if (c >= 'A' && c <= 'Z')
        c = c + 32;
    return (c);
}
int is_alpha(char c)
{
    if ((c >= 'a' && c <= 'z') ||  (c >= 'A' && c <= 'Z'))
        return (1);
    return (0);
}

int main(int argc, char **argv)
{
    int i;
    int j;
    char c;

    if (argc < 2)
        write(1, "\n", 1);
    i = 1;
    while (i < argc)
    {
        j = 0;
        while (argv[i][j])
        {
            c = to_lower(argv[i][j]);
            if (is_alpha(c) && (j == 0 || argv[i][j-1] == ' ' || argv[i][j-1] == '\t'))
               c = to_upper(c);
            write (1, &c, 1);
            j++;       
        }
        write(1, "\n", 1);
        i++;
    }
    return (0);
}
