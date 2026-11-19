#include <stdlib.h>

int	*ft_range(int start, int end)
{
	int	size;
	int	*array;
	int	i;

	if (start <= end)
		size = end - start + 1;
	else
		size = start - end + 1;

	array = (int *)malloc(sizeof(int) * size);
	if (!array)
		return (NULL);

	i = 0;
	if (start <= end)
	{
		while (i < size)
		{
			array[i] = start;
			start++;
			i++;
		}
	}
	else
	{
		while (i < size)
		{
			array[i] = start;
			start--;
			i++;
		}
	}
	return (array);
}
