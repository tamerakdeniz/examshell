


int ft_atoi(const char *str)
{
    int nb;
    int sign;

    nb = 0;
    sign = 1;
    while(*str == 32 || (*str >= 9 && *str <= 13))
        str++;
    if (*str == '-' || *str == '+')
    {
        if (*str == '-')
            sign = -1 * sign;
        str++;
    }
    while (*str >= '0' && *str <= '9')
    {
        nb = nb * 10 + (*str - '0');
        str++;
    }
    return (nb * sign);
}
