#include <iostream>
using namespace std;

struct Foo
{
    inline static Foo& Instance() {
        static Foo f;
        return f;
    }
    
    int i;
    Foo(): i(1) {}
};

int Max(int a, int b)
{
    return (a > b) ? a : b;
}

int main()
{
    cout << Foo::Instance().i << endl;
    cout << Max(1, 2) << endl;

    return 0;
}
