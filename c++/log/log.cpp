#include <cstdio>
//#include <cstring>
//#include <string>
//#include <unistd.h>
//#include <stdarg.h>
//#include <varargs.h>
//#include <errno.h>
#include "log.h"

using namespace std;

namespace Log
{

__thread Checkpoint* Checkpoint::s_pTop = NULL;


void PrintF_Internal(const char* szFmt, const long* pParams, const size_t nParamsCount, char* szBuf, size_t nLenBuf)
{
    //int nLen = vsnprintf(szBuf + nData, nLenBuf - nData - 3, szFmt, (va_list)pParams);
    //vsnprintf(szBuf, nLenBuf, szFmt, (va_list)pParams);
    //strcpy(szBuf + nLen + nData, "\n");
    // snprintf(szBuf, nLenBuf, szFmt);
    if (nParamsCount == 0)
        snprintf(szBuf, nLenBuf, szFmt);
    else
        snprintf(szBuf, nLenBuf, szFmt, pParams[0]);
    //snprintf(szBuf, nLenBuf, szFmt, pParams[0], pParams[nParamsCount - 1]);
        //snprintf(szBuf, nLenBuf, szFmt, pParams[0], pParams[1]);
        //snprintf(szBuf, nLenBuf, szFmt, pParams[0], pParams[1], pParams[2]);
        //snprintf(szBuf, nLenBuf, szFmt, (va_list)pParams);

    printf(szBuf);
}

void PrintCheckpoints()
{
    char sz[0x200];
    sz[0] = '\t';
    for (const Checkpoint* pCheckPoint = Checkpoint::s_pTop; pCheckPoint; pCheckPoint = pCheckPoint->m_pPrev)
        PrintF_Internal(pCheckPoint->m_szFmt, pCheckPoint->m_pParams, *(pCheckPoint->m_pParamsCount), sz, sizeof(sz));
}

void PrintF(const char* szFmt, const long* pParams, const size_t nParamsCount)
{
    char sz[0x200];
    PrintF_Internal(szFmt, pParams, nParamsCount, sz, sizeof(sz));
}

}
/*
void TestLog()
{
    {
        // 语句末可以加分号
        //CHECKPOINT("WorkerThread = %d\n" 
        //            << getpid());
        CHECKPOINT("WorkerThread = %d\n" 
                    << 12345);

        CHECKPOINT("Processing I/O\n")
        
        //string str("string");
        //CHECKPOINT("str: %s\n" << str.c_str());
    
        // CHECKPOINT 不能放在do while中，所以不能放在if中
        // 这么来看，CHECKPOINT的使用最好是在函数入口处。
        // 不然出了作用域，CHECKPINT就没了
        // 可以使用PUTLOG代替。
        //if (true)
        //    CHECKPOINT("str: %s\n" << str.c_str());

        {
            CHECKPOINT("Request from client ID = %d\n" << 246);

            {
                CHECKPOINT("Sending a file. Path = %s\n" << "/tmp/log");
                {
                    //PUTLOG("Can't open file. Error = %u\n" << errno);
                    Log::PrintCheckpoints();
                }
            }
        }
    }
}

int main()
{
    TestLog();

    return 0;
}
*/
