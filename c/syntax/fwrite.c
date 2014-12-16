#include <stdio.h>

void write_foo(FILE* dest)
{
    fwrite("c", 1, 1, dest);
}

int main()
{
    FILE* f = fopen("foo.txt", "w");
    // there is a buffer inside the fwrite implementation.
    printf("%d\n", BUFSIZ);             // 8192
    fwrite("a", 1, 1, f);
    fwrite("b", 1, 1, f);
    write_foo(f);
    fclose(f);

    return 0;
}
