#include <stdio.h>
#include <sys/time.h>
#include "logger.h"

namespace Logger
{

__thread Checkpoint* Checkpoint::s_pTop = NULL;

void LogUtil::PrintCheckpoints()
{
    SetCurTime();
    FILE* fp;
    fp = fopen(m_szLogFile, "a");
    int frame_num = 0;
    for (const Checkpoint* pCheckpoint = Checkpoint::s_pTop; pCheckpoint; pCheckpoint = pCheckpoint->m_pPrev) {
        const Record& rec = pCheckpoint->m_rRec;
        fprintf(fp, "%s [#%d][%s:%d--%s()] --- %s\n", m_szFmtTime, frame_num,
                            rec.m_szSrcFile, rec.m_nLineNumber, rec.m_szFuncName, rec.m_ssOstr.str().c_str());
        frame_num++;
    }
    fclose(fp);
}

void LogUtil::PrintLog(const Record& rec)
{
    SetCurTime();
    FILE* fp;
    fp = fopen(m_szLogFile, "a");
    fprintf(fp, "%s [%s:%d--%s()] --- %s\n", m_szFmtTime, 
                    rec.m_szSrcFile, rec.m_nLineNumber, rec.m_szFuncName, rec.m_ssOstr.str().c_str());
    fclose(fp);
}

void LogUtil::SetCurTime()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    struct tm* ptm;
    ptm = localtime(&(tv.tv_sec));
    strftime(m_szFmtTime, sizeof(m_szFmtTime), "%Y-%m-%d %H:%M:%S", ptm);
}

void LogUtil::SetLogFile()
{
    snprintf(m_szLogFile, 24, "class%d.log", 0);
}

} // namespace Logger
