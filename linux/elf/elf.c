#include <stdio.h>

int big_big_array[10 * 1024 * 1024];
char* a_string = "hello world!";
int a_global_var_with_value = 0x100;
int a_global_val_without_value;

int main()
{
    int a_local_val_with_value = 0x200;
    big_big_array[0] = 0x300;
    printf("%s\n", a_string);
    a_global_var_with_value += 1;

    return 0;
}
