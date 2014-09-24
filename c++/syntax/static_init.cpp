// zero initialization
// initial value of static object is 0.

#include <iostream>
using namespace std;

class Foo
{
public:
    int a;
    bool b;
    char c[12];

    static Foo& GetInstance()
    {
        static Foo f;
        return f;
    }
};

int main()
{
    Foo f = Foo::GetInstance();

    cout << f.a << endl;    // 0
    cout << f.b << endl;    // 0
    cout << f.c << endl;    // null

    return 0;
}
