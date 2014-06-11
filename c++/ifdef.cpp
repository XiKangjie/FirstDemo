#include <stdio.h>


int main()
{
#ifdef FOO
    printf("foo 1\n");
    printf("foo 2\n");
#else
    printf("no 1\n");
    printf("no 2\n");
#endif

    return 0;
}
