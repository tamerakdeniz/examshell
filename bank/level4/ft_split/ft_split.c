
#include <stdlib.h>

int is_space(char c)
{
    if (c == ' ' || c >= 9 && c <= 13)
        return 1;
    return 0;
}

int count_word(char *s)
{
    int i;
    int count;

    i = 0;
    count = 0;
    while(s[i])
    {
        while(s[i] && is_space(s[i]))
            i++;
        if (s[i])
            count++;
        while (s[i] && !is_space(s[i]))
            i++;
    }
    return(count);
}

char *word_dup(char *s, int start, int end)
{
    char *word;
    int i;

    word = malloc(end - start + 1);
    if (!word)
        return NULL;
    i = 0;
    while (start < end)
        word[i++] = s[start++];
    word[i] = '\0';
    return (word);
}

char    **ft_split(char *str)
{
    char **res;
    int i;
    int j;
    int start;
    
    res = malloc(sizeof(char *) * (count_word(str) + 1));
    if (!res)
        return NULL;
    i = 0;
    j = 0;
    while (str[i])
    {
        while(str[i] && is_space(str[i]))
            i++;
        start = i;
        while(str[i] && !is_space(str[i]))
            i++;
        if (i > start)
            res[j++] = word_dup(str, start, i);
    }
    res[j] = NULL;
    return (res);
}