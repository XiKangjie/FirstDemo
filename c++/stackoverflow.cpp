#include <stdio.h>
#include <string.h>

int main()
{
    int len = 0;
    char str[10] = {0};
    printf("addr len: %p\n", &len);
    printf("addr str[0]: %p\n", &str[0]);
    printf("addr str[1]: %p\n", &str[1]);
    printf("size of ptr: %ld\n", sizeof(long unsigned int));
    printf("addr len - addr str: %ld", (long unsigned int)(&len) -(long unsigned int)(&str[0]));
    printf("\nlen initial value:%d\n", len);
    printf("\nEnter the name:\n");
    gets(str);  // use gets() to cause buffer overflow

    printf("\nnow len = %d\n", len);

    len = strlen(str);
    printf("len of string entered is: %d\n", len);


    return 0;
}
