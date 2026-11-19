#include <unistd.h>

int main(int ac, char **av)
{
    int seen[256] = {0};
    int i = 1;
    int j;
    char c;

    if (ac == 3)
    {
        while (i <= 2)
        {
            j = 0;
            while (av[i][j])
            {
                c = av[i][j++];
                if (!seen[(unsigned char)c])
                {
                    write(1, &c, 1);
                    seen[(unsigned char)c] = 1;
                }
            }
            i++;
        }
    }
    write(1, "\n", 1);
}
