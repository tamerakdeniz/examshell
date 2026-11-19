#include <stdlib.h>

int *ft_rrange(int start, int end)
{
    int size = end - start;
    int i = 0;
    int step = 1;
    int *range;

    if (size < 0)
        size = -size;
    size++;
    range = malloc(size * sizeof(int));
    if (!range)
        return (NULL);
    if (end > start)
        step = -1;
    while (i < size)
    {
        range[i] = end + i * step;
        i++;
    }
    return (range);
}
