#include <cstdio>
#include <stdarg.h>
using namespace std;

/*
namespace Log
{

struct CheckPoint
{
    //static Checkpoint* s_pTop;
    //Checkpoint* m_pPrev;
    const char m_fmt;
    va_list m_ap;

    CheckPoint(const char* fmt, ...)
    {
        m_fmt = fmt;
        va_start(m_ap, m_fmt);
    }

    void output()
    {
        char buf[124];
        vsnprintf(buf, 124, m_fmt, m_ap);
        printf(buf);
        va_end(m_ap);
    }
};

}
*/
/*
struct Record
{
    va_list ap;
    void check(const char* fmt, ...)
    {
        va_start(ap, fmt);
    }
    void output()
    {
        char buf[124];
        vsnprintf(buf, 124, fmt, ap);
        printf(buf);
        va_end(ap);
    }
};

*/
va_list g_ap;
const char* g_fmt;
void foo(const char* fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    va_copy(g_ap, ap);
    g_fmt = fmt;
    char buf[124];
    vsnprintf(buf, 124, g_fmt, ap);
    printf(buf);
    //va_end(ap);
}
void bar()
{
    char buf[124];
    //va_start(g_ap, g_fmt);
    vsnprintf(buf, 124, g_fmt, g_ap);
    printf(buf);
    va_end(g_ap);
}
int main()
{
    foo("help: %d\n", 110);
    bar();
    
    //Log::CheckPoint cp("help: %d\n", 120);
    //cp.output();

    return 0;
}
