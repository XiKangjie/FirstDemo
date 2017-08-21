#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[2] = {1, 2};
    int *p = a;
    printf("%d\n", *p++);       // 1

    char buf[128];
    char* path = "/etc////passwd";
    if(realpath(path, buf))
        printf("%s\n", buf);    // /etc/passwd

    path = "level00.c";
    if(realpath(path, buf))
        printf("%s\n", buf);    // /home/fusion/demo/security/fusion/level00/level00.c

    return 0;
}
