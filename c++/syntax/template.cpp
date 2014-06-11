#include <iostream>
using namespace std;

struct Size
{
    int size;
    Size() : size(-1) {}

    Size& operator << (const char*)
    {
        size++;
        return *this;
    }

    template <typename T>
    Size& operator << (const T&)
    {
        size++;
        return *this;
    }
};

template <size_t nSize> 
struct Record 
{
    const char* m_szFmt;
    int m_pParmas[nSize];
};


struct SizeCalc
{
    template <size_t nSize>
    struct Nested
    {
        char m_pBuf[nSize];
        Nested<nSize + 1> operator << (const char*);
        template <typename T> Nested<nSize + 1> operator << (const T&);
    };
    Nested<0> operator << (const char* szFmt);
};

int main()
{
    Size s;
    s << "name: %s, age: %d\n" << "xikangjie" << 18;
    cout << s.size << endl;

    int array[s.size];
    //array[0] = 1; array[1] = 2;
    int* p = array;
    *((int*)p) = 1;
    *((int*)(p + 1)) = 2;
    cout << array[0] << endl << array[1] << endl;

    int array2[2] = {1, 2};
    cout << array2[0] << endl << array2[1] << endl;

    // Record<s.size> rec;          // error
    // Record<sizeof(array)> rec;   // error
    Record<sizeof(array2)> rec2;    // ok
    // Record<5> rec;                  // ok
    Record<sizeof(SizeCalc() << "name: %s" << "xikangjie")> rec;    // ok
    

    return 0;
}
