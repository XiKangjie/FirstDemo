#include <iostream>
#include <map>
using namespace std;

class Foo
{
public:
    typedef map<int, int> Map;
    static inline void print() { cout << i << endl; }
    static inline void insert(int k, int b) { m[k] = b; cout << m[k] << endl; }
private:
    static int i;
    static Map  m;
};

Foo::Map Foo::m;
int Foo::i = 0;

int main()
{
    Foo f;
    f.print();
    Foo::print();

    Foo::insert(1, 1);
    f.insert(2, 2);

    return 0;
}
