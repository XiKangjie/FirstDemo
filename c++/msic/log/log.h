#ifndef LOG_H
#define LOG_H
#include <pthread.h>

namespace Log
{
template <typename T>
struct StackAligned
{
    long m_pBuf[(sizeof(T) + sizeof(long)-1) / sizeof(long)];
};
struct Feed
{
    long* m_pPtr;
    template <typename T> void Consume(const T& val) {
        *((T*) m_pPtr) = val;
        //m_pPtr += sizeof(StackAligned<T>) / sizeof(long);
        m_pPtr++;
    }

    template <typename T> Feed& operator << (const T& val) {
        Consume(val);
        return *this;
    }
    Feed& operator << (const char* val) {
        Consume<const char*>(val);
        return *this;
    }
};

template <size_t nSize>
struct Record
{
    const char* m_szFmt;
    // long m_pParams[nSize / sizeof(long)];
    long m_pParams[nSize];
    const size_t m_nParamsCount;

    //Record() : m_nParamsCount(nSize / sizeof(long)) {}
    Record() : m_nParamsCount(nSize) {}
    
    Feed operator << (const char* szFmt) {
        m_szFmt = szFmt;
        Feed feed;
        feed.m_pPtr = m_pParams;
        return feed;
    }
};

struct SizeCalc
{
    template <size_t nSize>
    struct Nested
    {
        char m_pBuf[nSize];
        Nested<nSize + sizeof(StackAligned<const char*>)> operator << (const char*);
        template <typename T> Nested<nSize + sizeof(StackAligned<T>)> operator << (const T&);
    };
    Nested<0> operator << (const char* szFmt);
};
/*
struct SizeCalc
{
   int m_nSize;
   SizeCalc(): m_nSize(-1) {}

   SizeCalc& operator << (const char*)
   {
       m_nSize++;
       return *this;
   }
   template <typename T>
   SizeCalc& operator << (const T&)
   {
       m_nSize++;
       return *this;
   }
};
*/
void PrintF(const char* szFmt, const long* pParams, const size_t nParamsCount);

struct Checkpoint
{
    static __thread Checkpoint* s_pTop;
    Checkpoint* m_pPrev;
    const char* m_szFmt;
    const long* m_pParams;
    const size_t* m_pParamsCount;

    template <size_t nSize>
    Checkpoint(const Record<nSize>& rec)
        :m_szFmt(rec.m_szFmt)
        ,m_pParams(rec.m_pParams)
        ,m_pParamsCount(&rec.m_nParamsCount)
    {
        m_pPrev = s_pTop;
        s_pTop = this;
    }

    ~Checkpoint()
    {
        s_pTop = m_pPrev;
    }
};

void PrintCheckpoints();

} // namespace Log

// Internally-used macro
#define BUILD_FMT_RECORD(rec, expr) \
    Log::Record<sizeof(Log::SizeCalc() << expr)> rec; \
    rec << expr; \

// Macros to generate random identifiers
#define RAND_IDENTIFIER_2(x, y) x##y
#define RAND_IDENTIFIER_1(x, y) RAND_IDENTIFIER_2(x, y)
#define RAND_IDENTIFIER(prefix) RAND_IDENTIFIER_1(prefix, __LINE__)

// Put this in the log
#define PUTLOG(expr) \
    do { \
        BUILD_FMT_RECORD(RAND_IDENTIFIER(recAutoToLog), expr) \
        Log::PrintF(RAND_IDENTIFIER(recAutoToLog).m_szFmt, RAND_IDENTIFIER(recAutoToLog).m_pParams, RAND_IDENTIFIER(recAutoToLog).m_nParamsCount); \
    } while(false)

// Declare a checkpoint
#define CHECKPOINT(expr) \
    BUILD_FMT_RECORD(RAND_IDENTIFIER(var##_Record), expr) \
    Log::Checkpoint RAND_IDENTIFIER(var)(RAND_IDENTIFIER(var##_Record)); \

#endif // LOG_H
