#include <iostream>
using namespace std;

struct Foo
{
    int bar;
    Foo(): bar(0) {}
};

int main()
{
    Foo f;
    cout << f.bar << endl;
    
    return 0;
}
