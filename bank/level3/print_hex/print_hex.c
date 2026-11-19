
#include <unistd.h>

void print_hex(unsigned int n)
{
    char *hex = "0123456789abcdef";

    if(n >= 16)
        print_hex(n / 16);
    write(1, &hex[n%16], 1);
}
int ft_atoi(char *str)
{
    int n;

    n = 0;
    while (*str)
    {
        n = n * 10 + (*str - '0');
        str++;
    }
    return(n);
}

int main(int ac, char **ag)
{
    if (ac == 2)
        print_hex(ft_atoi(ag[1]));
    write(1, "\n", 1);
    return 0;
}