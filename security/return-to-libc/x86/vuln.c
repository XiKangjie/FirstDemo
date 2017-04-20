//vuln.c
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    setuid(0);
    printf("%d\n", getuid());

    char buf[256];
    printf("%p\n", buf);
    strcpy(buf,argv[1]);
    printf("%s\n",buf);

    fflush(stdout);

    return 0;
}
