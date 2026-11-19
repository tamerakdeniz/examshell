#include <stdlib.h>

static int is_space(char c)
{
    return (c == ' ' || c == '\t' || c == '\n');
}

char **ft_split(char *str)
{
    int i = 0;
    int count = 0;
    int len;
    int j;
    char **words;

    while (str[i])
    {
        if (!is_space(str[i]) && (i == 0 || is_space(str[i - 1])))
            count++;
        i++;
    }
    words = malloc((count + 1) * sizeof(char *));
    if (!words)
        return (NULL);
    i = 0;
    while (*str)
    {
        while (is_space(*str))
            str++;
        if (!*str)
            break;
        len = 0;
        while (str[len] && !is_space(str[len]))
            len++;
        words[i] = malloc(len + 1);
        if (!words[i])
            break;
        j = 0;
        while (j < len)
            words[i][j++] = *str++;
        words[i++][len] = '\0';
    }
    words[i] = NULL;
    return (words);
}
