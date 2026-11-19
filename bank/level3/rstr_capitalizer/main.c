#include <unistd.h>

int main(int ac, char **av)
{
    int i = 1;
    int j;

    if (ac == 1)
        write(1, "\n", 1);
    while (i < ac)
    {
        j = 0;
        while (av[i][j])
        {
            if (av[i][j] >= 'A' && av[i][j] <= 'Z')
                av[i][j] += 32;
            if (av[i][j] >= 'a' && av[i][j] <= 'z' && (av[i][j + 1] == '\0' || av[i][j + 1] == ' ' || av[i][j + 1] == '\t'))
                av[i][j] -= 32;
            write(1, &av[i][j], 1);
            j++;
        }
        write(1, "\n", 1);
        i++;
    }
}


// int main(int argc, char **argv)
// {
//     int arg = 1;
//     int i;
//     char *str;

//     if (argc == 1)
//         write(1, "\n", 1);
//     while (arg < argc)
//     {
//         str = argv[arg++];
//         i = 0;
//         while (str[i])
//         {
//             if (str[i] >= 'A' && str[i] <= 'Z')
//                 str[i] += 32;
//             if (str[i] >= 'a' && str[i] <= 'z'
//                 && (!str[i + 1] || str[i + 1] == ' ' || str[i + 1] == '\t'))
//                 str[i] -= 32;
//             write(1, &str[i++], 1);
//         }
//         write(1, "\n", 1);
//     }
//     return (0);
// }
