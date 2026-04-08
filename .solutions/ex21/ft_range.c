#include <stdlib.h>

int *ft_range(int min, int max)
{
    int *arr;
    int i, n;

    if (min >= max)
        return NULL;
    n = max - min;
    arr = (int *)malloc(n * sizeof(int));
    if (!arr)
        return NULL;
    i = 0;
    while (i < n)
    {
        arr[i] = min + i;
        i++;
    }
    return arr;
}
