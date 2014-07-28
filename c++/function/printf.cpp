#include <stdio.h>

int main()
{
    // first line, 1,            second line, 2
    printf("first line, %d,\
            second line, %d\n", 1, 2);

    // printf return the number of characters printed
    int i=43;
    printf("%d\n",printf("%d",printf("%d",i)));     // 4321

    return 0;
}
