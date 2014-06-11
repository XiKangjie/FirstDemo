#include <cstdio>
#include <sstream>
using namespace std;
/*
void mysnprintf(const char* buf, const int buflen, const char* fmt, long* para = NULL, int count = 0)
{
    int i = 0, j = 0;
    int len = 0;
    for (int i = 0; i < count; i++) {
        len = snprintf(buf + len, buflen, fmt, para[i]);
        buflen -= len;
        while(fmt[j] !=)
    }
}
*/

int main()
{
    char buf[256];
    int len = snprintf(buf, 124, "name%: %s, age: %d\n", "xikangjie", 18);
    printf(buf);
    printf("len : %d\n", len);      // 25 '\n'

    long para[256] = {0};
    char* name = "xikangjie";
    *((char**)para) = name;
    *((int*)(para+1)) = 18;
    *((double*)(para+2)) = 1111.111;
    snprintf(buf, 124, "name: %s, age: %d, %f\n", para[0], para[1], *(double*)(para+2));    // 必须做转换i,(double)(para[2])不可以
    printf(buf);

    long params[12] = {0};
    *((char**)params) = "name: ";
    *((char**)(params + 1)) = "xikangjie,";
    *((char**)(params + 2)) = "age: ";
    *((int*)(params + 3)) = 18;
    *((char**)(params + 4)) = " blabla ";
    *((long*)(params + 5)) = 11111111111;
    *((double*)(params + 6)) = 111.11;
    ostringstream ostr;
    ostr << (char*)params[0] << (char*)params[1] << (char*)params[2]
         << params[3] << (char*)params[4] << params[5] << params[6]<< endl;
    printf(ostr.str().c_str());

    ostr << "name " << 123 << 111.1 << endl;
    printf(ostr.str().c_str());

    return 0;
}
