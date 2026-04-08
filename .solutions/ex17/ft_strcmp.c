int ft_strcmp(char *s1, char *s2)
{
    unsigned char a, b;

    while (*s1 && (*s1 == *s2))
    {
        s1++;
        s2++;
    }
    a = (unsigned char)*s1;
    b = (unsigned char)*s2;
    return (int)(a - b);
}
