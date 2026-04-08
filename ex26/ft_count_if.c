int ft_count_if(char **tab, int (*f)(char*))
{
    int i = 0;
    int cnt = 0;

    if (!tab || !f)
        return 0;
    while (tab[i])
    {
        if (f(tab[i]))
            cnt++;
        i++;
    }
    return cnt;
}
