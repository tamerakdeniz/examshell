
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
                    write(1, " ", 1);
                flag = 0;
                write (1, &ag[1][i], 1);
            }
            i++;
        }
    }
    write (1, "\n", 1);
    return 0;
}

// #include <unistd.h>

// int main(int ac, char **av)
// {
//     int i;
//     int word;

//     if (ac == 2)
//     {
//         i = 0;
//         word = 0;
//         while (av[1][i])
//         {
//             while (av[1][i] == ' ' || av[1][i] == '\t')
//                 i++;
//             if (av[1][i] && word)
//                 write(1, " ", 1);
//             while (av[1][i] && av[1][i] != ' ' && av[1][i] != '\t')
//             {
//                 write(1, &av[1][i], 1);
//                 i++;
//                 word = 1;
//             }
//         }
//     }
//     write(1, "\n", 1);
//     return (0);
// }