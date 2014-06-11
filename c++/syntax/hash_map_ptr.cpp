#include <iostream>
#include <hash_map>
using namespace std;

struct Foo
{
    int foo1;
    bool foo2;
    Foo(): foo1(0), foo2(false) {}
};

struct Count
{
    int cnt1;
    int cnt2;
    Count(): cnt1(0), cnt2(0) {}
};

Foo f[10];

int main()
{
    // hash_map<int, int> test;
    
    hash_map<void*, Count> m;
    Count c;
    for (int i = 0; i < 5; i++) {
        m[&f[i]] = c;
    }
    m[&f[0]].cnt1++;
    hash_map<void*, Count>::iterator it = m.begin();
    cout << it->first << endl;
    it++;
    cout << it->first << endl;

    cout << m[&f[0]].cnt1 << endl;
    
    m[&f[5]].cnt1++;
    cout << m[&f[5]].cnt1 << endl;

    return 0;
}
