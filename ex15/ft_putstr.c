void ft_putchar(char c);

void ft_putstr(char *str)
{
    while (str && *str)
        ft_putchar(*str++);
}
