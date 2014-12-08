#include <stdio.h>

void common_print(const char *s) __attribute__((weak));
void print_a(const char *s) __attribute__((weak, alias("common_print")));
void print_b(const char *s) __attribute__((weak, alias("common_print")));

void common_print(const char *s)
{
    printf("lib print: %s\n", s);
}
