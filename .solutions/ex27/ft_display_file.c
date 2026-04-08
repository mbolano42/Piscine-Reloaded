#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    int fd;
    ssize_t r;
    char buf[4096];

    if (argc == 1)
    {
        write(2, "File name missing.\n", 19);
        return 1;
    }
    if (argc > 2)
    {
        write(2, "Too many arguments.\n", 20);
        return 1;
    }
    fd = open(argv[1], O_RDONLY);
    if (fd < 0)
    {
        /* "Cannot read file.\n" is 18 bytes (no NUL). write should not include the trailing NUL. */
        write(2, "Cannot read file.\n", 18);
        return 1;
    }
    while ((r = read(fd, buf, sizeof(buf))) > 0)
    {
        ssize_t w = write(1, buf, r);
        (void)w;
    }
    close(fd);
    return 0;
}
