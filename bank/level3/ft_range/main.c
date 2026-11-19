#include <stdlib.h>

int *ft_range(int start, int end)
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
    if (start > end)
        step = -1;
    while (i < size)
    {
        range[i] = start + i * step;
        i++;
    }
    return (range);
}
