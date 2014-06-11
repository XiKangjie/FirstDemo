#ifndef NSFOCUS_LOGGER_H
#define NSFOCUS_LOGGER_H

#include <pthread.h>
#include <assert.h>
#include <sstream>

namespace Logger
{

struct Record
{
    std::ostringstream m_ssOstr;
    const int m_nLineNumber;
    const char* m_szFuncName;
    const char* m_szSrcFile;

    Record(const int line, const char* func, const char* file)
        : m_nLineNumber(line), m_szFuncName(func), m_szSrcFile(file) {}
};

struct Checkpoint
{
    static __thread Checkpoint* s_pTop;
    Checkpoint* m_pPrev;
    const Record& m_rRec;

    Checkpoint(const Record& rec): m_rRec(rec){
        m_pPrev = s_pTop;
        s_pTop = this;
    }

    ~Checkpoint() {
        assert(this == s_pTop);
        s_pTop = m_pPrev;
    }
};

class LogUtil
{
public:
    static LogUtil& GetInstance() {
        static LogUtil instance;
        return instance;
    }

    void PrintCheckpoints();
    void PrintLog(const Record& rec);


private:
    LogUtil() {
        SetLogFile();
    }
    LogUtil(const LogUtil&) {}
    LogUtil& operator = (LogUtil const&) {}

    void SetCurTime();
    void SetLogFile();  // ?

    char m_szFmtTime[24];
    char m_szLogFile[24];

};

}   // namespace Logger

// Macros to generate random identifiers
#define RAND_IDENTIFIER_2(x, y) x##y
#define RAND_IDENTIFIER_1(x, y) RAND_IDENTIFIER_2(x, y)
#define RAND_IDENTIFIER(prefix) RAND_IDENTIFIER_1(prefix, __LINE__)

#define BUILD_RECORD(rec, expr) \
    Logger::Record rec(__LINE__, __FUNCTION__, __FILE__); \
    rec.m_ssOstr << expr;

// Put this in the log
#define OUTPUTLOG(expr) \
do { \
    BUILD_RECORD(RAND_IDENTIFIER(rec), expr) \
    Logger::LogUtil::GetInstance().PrintLog(RAND_IDENTIFIER(rec)); \
} while(false)

// Declare a checkpoint
#define CHECKPOINT(expr) \
    BUILD_RECORD(RAND_IDENTIFIER(var##_rec), expr) \
    Logger::Checkpoint RAND_IDENTIFIER(var)(RAND_IDENTIFIER(var##_rec));

#define PRINTCHECKPOINTS() Logger::LogUtil::GetInstance().PrintCheckpoints();

#endif  // NSFOCUS_LOGGER_H
