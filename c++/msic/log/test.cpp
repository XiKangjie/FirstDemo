#include <sstream>
#include <stdio.h>
#include "log.h"
using namespace std;

__thread Log::Checkpoint* Log::Checkpoint::s_pTop = NULL;

int main()
{
    Log::Record<sizeof(Log::SizeCalc() << "WorkerThread = %d" << 123)> var_Record40;
    var_Record40 << "WorkerThread = %d" << 123;
    Log::Checkpoint var40(var_Record40);
    
    printf("fmt: %s\n", var40.m_szFmt);
    printf("para: %d\n", *(var40.m_pParams));

    Log::Record<sizeof(Log::SizeCalc() << "Sending a file. Path = %s" << "/tmp/log")> var_Record48;
    var_Record48 << "Sending a file. Path = %s" << "/tmp/log"; 
    Log::Checkpoint var48(var_Record48);
    printf("fmt: %s\n", var48.m_szFmt);
    /*
    ostringstream ostr;
    ostr << var48.m_pParams;
    printf("para: %s\n", ostr.str().c_str());
    */
    printf("para: %s\n", (const char*)var48.m_pParams);
  
  return 0;
}

