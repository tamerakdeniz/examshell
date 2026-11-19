#include <unistd.h>

int main(int ac, char **av)
{
    int i;
    int j;
    int l;
    if (ac == 3)
    {
        i = 0;
        while (av[1][i])
        {
            l = 0;
            while (l < i && av[1][l] != av[1][i])
                l++;
            if (l == i)
            {
                j = 0;
                while (av[2][j])
                {
                    if (av[1][i] == av[2][j])
                    {
                        write(1, &av[1][i], 1);
                        break;
                    }
                    j++;
                }
            }
            i++;
        }
    }
    write(1, "\n", 1);
}
