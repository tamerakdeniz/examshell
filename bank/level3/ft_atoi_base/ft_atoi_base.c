
int	ft_atoi_base(const char *str, int base)
{
    int nb;
    int sign;
    int value;

    sign = 1;
    if (*str == '+' || *str == '-')
    {
        if (*str == '-')
            sign = -1 *sign;
        str++;
    }
    nb = 0;
    while (*str)
    {
        if (*str >= '0' && *str <= '9')
            value = *str - '0';
        else if (*str >= 'A' && *str <= 'F')
            value = *str - 'A' + 10;
        else if (*str >= 'a' && *str <= 'f')
            value = *str - 'a' + 10;
        else
            break;
        if (value >= base)
            break;
        nb = nb * base + value;
        str++;
    }
    return(sign * nb);
}
