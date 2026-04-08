#include <stdlib.h>
#include <string.h>

char *ft_strdup(char *src)
{
    char *p;
    size_t len;

    if (!src)
        return NULL;
    len = strlen(src);
    p = (char *)malloc(len + 1);
    if (!p)
        return NULL;
    memcpy(p, src, len + 1);
    return p;
}
