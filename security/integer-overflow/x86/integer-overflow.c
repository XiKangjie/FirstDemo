#include <stdio.h>

int main()
{
    unsigned char uc1 = 0xff;
    printf("uc1: %x, %d\n", uc1, uc1);
    printf("uc1 + 1: 0x%x, %d\n", uc1 + 1, uc1 + 1);
    printf("uc1 + 2: 0x%x, %d\n", uc1 + 2, uc1 + 2);

    char c1 = 0x7f;
    printf("c1: %x, %d\n", c1, c1);
    printf("c1 + 1: 0x%x, %d\n", c1 + 1, c1 + 1);
    printf("c1 + 2: 0x%x, %d\n", c1 + 2, c1 + 2);
    printf("0x8f + 0x8f: 0x%x, %d\n", 0x8f + 0x8f, 0x8f + 0x8f);

    return 0;
}
