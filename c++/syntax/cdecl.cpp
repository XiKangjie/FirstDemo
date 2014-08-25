#include <stdio.h>
#include <string.h>
#include <iostream>

char* foo(const char* s)
{
    static char buf[32];
    strcpy(buf, s);
    return buf;
}

int main()
{
    printf("str1: %s, str2: %s\n", foo("hello"), foo("world"));
    std::cout << foo("hello") << foo("world") << std::endl;

    return 0;
}

// str1: hello, str2: hello
// hellohello
