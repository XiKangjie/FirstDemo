#include <stdio.h>

void foo()
{
    printf("func: %s, line: %d, file:%s\n", __FUNCTION__, __LINE__, __FILE__);
}

void printFunc(const char* fun)
{
    printf("func: %s\n", fun);
}

void printFile(const char* file)
{
    printf("file: %s\n", file);
}

void printLine(const int line)
{
    printf("line: %d\n", line);
}

struct Func
{
    const char* func;
    Func(const char* f): func(f) {}
};

#define LOG_ERR \
    if (false) \
        printf("wow\n")

int main()
{   
    printf("func: %s, line: %d, file:%s\n", __FUNCTION__, __LINE__, __FILE__);
    foo();
    printFunc(__FUNCTION__);
    printFile(__FILE__);
    printLine(__LINE__);
    const char* str = __FUNCTION__;
    printFunc(str);

    Func f(__FUNCTION__);
    printFunc(f.func);

    if (true)
        LOG_ERR;
    else
        printf("else\n");

    return 0;
}
