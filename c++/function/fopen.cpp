#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("BUFSIZ: %d\n", BUFSIZ);

    FILE* f;
    f = fopen("fopen.txt", "w");
    char buf[120];
    setvbuf(f, buf, _IOFBF, 100);
    printf("BUFSIZ: %d\n", BUFSIZ);
    if (f) {
        char buffer[] = "0123456789";
        printf("write ...\n");
        fwrite(buffer, sizeof(char), sizeof(buffer), f);
        printf("sleeep 10s ...\n");
        sleep(10);
        fclose(f);
    }

    return 0;
}
