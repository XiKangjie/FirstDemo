#include <iostream>
#include <hash_map>
#include <unistd.h>
using namespace std;

struct Foo {
    char c[1024];
};

typedef hash_map<int, Foo> FooMap;
typedef hash_map<int, FooMap> MMap;

int main()
{
    MMap h;
    h[0];
    for (int i = 0; i < 1024 * 100; i++) {
        h[0][i];
    }
    cout << "init end, sleep 10s" << endl;
    cout << "h[0] size: " << h[0].size() << endl;
    cout << "h[0] bucket_count: " << h[0].bucket_count() << endl;
    sleep(10);
    h.clear();      // clear() releases h's memory.
    cout << "clear, sleep 30s" << endl;
    cout << "h[0] size: " << h[0].size() << endl;
    cout << "h[0] bucket_count: " << h[0].bucket_count() << endl;
    sleep(30);

    return 0;
}
