#include <iostream>
#include <set>
using namespace std;

struct Foo
{
    int a;
    int array[4];
    set<int> s;
};

int main()
{
    Foo* f = new Foo;
    f->s.insert(1);
    cout << f->a << endl;
    for (int i = 0; i < 4; i++)
    {
        cout << f->array[i] << endl;
    }

    cout << sizeof(Foo) << endl;
    Foo* p = (Foo*)(new int[sizeof(Foo)]);
    new (p) Foo();
    cout << p->a << endl;
    for (int i = 0; i < 4; i++)
    {
        cout << p->array[i] << endl;
    }


    return 0;
}
