#include <stdio.h>
#include <sys/stat.h>

int main()
{
    struct stat st;
    stat("open.txt", &st);
    printf("open.txt size: %d\n", st.st_size);

    return 0;
}
