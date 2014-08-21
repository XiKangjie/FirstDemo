#include <stdarg.h>
#include <stdio.h>
#include <string>

#define PRINT( module, level, fmt, ...)\
    Print(module, level, __FILE__, __LINE__, __FUNCTION__, fmt, ##__VA_ARGS__);

void Print(int module, int level, const char* src, const int line, const char* func,
        const char* fmt, ...)
{
    char buf[512];
    int dec_n = snprintf(buf, 512, "%d.%d %s:%d %s() --- ", module, level, src, line, func);
    va_list vl;
    va_start(vl, fmt);
    char* pc = va_arg(vl, char*);
    printf("arg1: %s\n", pc);
    va_end(vl);

    //va_start(vl, fmt);
    char* pc2 = va_arg(vl, char*);
    printf("arg2: %s\n", pc2);
    //va_end(vl);

    va_start(vl, fmt);
    int msg_n = vsnprintf(buf + dec_n, 512 - dec_n, fmt, vl);
    printf("%s", buf);
    va_end(vl);
}

int main()
{
    std::string str1 = "1.1.1.1";
    std::string str2 = "2.2.2.2";
    PRINT(1, 1, "%s %s\n", str1.c_str(), str2.c_str());
    return 0;
}

//iarg1: 1.1.1.1
//arg2: 2.2.2.2
//1.1 vsnprintf.cpp:34 main() --- 1.1.1.1 2.2.2.2
