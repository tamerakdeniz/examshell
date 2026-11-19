int ft_atoi_base(const char *str, int str_base)
{
    int sign = 1;
    int digit;
    long result = 0;

    if (str_base < 2 || str_base > 16)
        return (0);
    if (*str == '-' || *str == '+')
    {
        if (*str == '-')
            sign = -1;
        str++;
    }
    while (*str)
    {
        if (*str >= '0' && *str <= '9')
            digit = *str - '0';
        else if (*str >= 'a' && *str <= 'f')
            digit = *str - 'a' + 10;
        else if (*str >= 'A' && *str <= 'F')
            digit = *str - 'A' + 10;
        else
            break;
        if (digit >= str_base)
            break;
        result = result * str_base + digit;
        str++;
    }
    return (result * sign);
}
