#include <stdio.h>
#include <unistd.h> // write close
#include <fcntl.h>  // O_APPEND

int main()
{   
    int fd;
    fd = open("./open.txt", O_WRONLY/* |O_CREAT*/ | O_APPEND, 0644);
    //fd = open("/dev/pts/31", O_WRONLY | O_CREAT | O_APPEND, 0644);
    if (fd < 0) {
        printf("fd: %d\n", fd);
        //return 0;
    }
    printf("sleep 5s\n");
    sleep(5);
    int n = write(fd, "test\n", 5);
    printf("n: %d\n", n);
    close(fd);

    return 0;
}
