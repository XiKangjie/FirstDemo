#include <stdio.h>
#include <string.h>
#include <string>

int main()
{
    std::string str("test");
    char str2[12];
    strncpy(str2, str.c_str(), str.length());
    
    printf(str2);

    return 0;
}
