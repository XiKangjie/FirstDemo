/*
 * gcc -o gcc_strong.exe gcc_strong.c gcc_weak.c
 */

#include <stdio.h>

void common_print(const char *s)
{
    printf("application common_print: %s\n", s);
}

void print_a(const char *s)
{
    printf("application print_a: %s\n", s);
}

int main()
{
    common_print("test");

    print_a("test a");
    print_b("test b");

    return 0;
}

/*

application common_print: test
application print_a: test a
lib print: test b

*/
