
int	ft_atoi(const char *str)
{
    long nb = 0;
    int sign = 1;
    while ((*str >= 9 && *str <= 13) || *str == ' ')
        str++;
    if (*str == '-' || *str == '+')
    {
        if (*str == '-')
            sign *= -1;
        str++;
    }
    while (*str >= '0' && *str <= '9')
        nb = nb * 10 + (*str++ - '0');
    return (nb * sign);
}