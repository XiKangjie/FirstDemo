#include <stdio.h>

struct Demo {};

int main()
{
    struct Demo d;
    printf("size of empty struct d: %lu\n", sizeof(d));

    struct Demo d2;
    printf("addr of empty struct d: %p\n", &d);
    printf("addr of empty struct d2: %p\n", &d2);

    return 0;
}

/*

0
0x7ffff42f6660
0x7ffff42f6660

*/
