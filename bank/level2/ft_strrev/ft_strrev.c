
char *ft_strrev(char *str)
{
    int i;
    int j;
    char tmp;

    i = 0;
    j = 0;
    while (str[i])
        i++;
    i--; // NULL icin
    while (j < i)
    {
        tmp = str[j];
        str[j] = str[i];
        str[i] = tmp;
        j++;
        i--;
    }
    return (str);
}