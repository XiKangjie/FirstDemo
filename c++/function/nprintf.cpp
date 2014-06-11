#include <stdio.h>
#include <stdarg.h>

int print(const char* fmt, ...)
{
    char buf[8];
    va_list args;
    va_start(args, fmt);
    int n = vsnprintf(buf, 8, fmt, args);
    if (n <= 0) {
        printf("error, n = %d\n", n);
    }
    else {
        printf("buf: %s, n: %d\n", buf, n);
    }
    va_end(args);
}


int main()
{
    char buf[16] = {'1', 0};
    int n = snprintf(buf, 16, "123%d", 456789);
    if (n <= 0) {
        printf("error, n = %d\n", n);
    }
    else {
        printf("buf: %s, n: %d\n", buf, n);
    }

    print("123%d", 456789);

    return 0;
}
