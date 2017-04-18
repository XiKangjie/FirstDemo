//vuln.c
#include <stdio.h>
#include <string.h>

void foo(char* arg);
void bar(char* arg);

void foo(char* arg) {
    int a;
    printf("a: %p\n", &a);
    bar(arg);
}

void bar(char* arg) {
    char buf[256];
    printf("buf: %p\n", buf);
    strcpy(buf, arg);
}

int main(int argc, char *argv[]) {
    if(strlen(argv[1]) > 256) {
        printf("Attempted Buffer Overflow\n");
        return -1;
    }

    setuid(0);

    foo(argv[1]);

    return 0;
}
