// gperftools heap profiler
// g++ -o heap_profiler.exe heap_profiler.cpp -I /usr/include/stlport/ -lstlport -ltcmalloc
// HEAPPROFILE=heappro ./heap_profiler.exe
// pprof ./heap_profiler.exe heappro.0001.heap > heappro.0001.text

#include <iostream>
#include <hash_map>
using namespace std;

struct Foo
{
    int size;
    char buf[1024 * 1024];
};

int main()
{
    hash_map<int, Foo> m;
    
    for (int i = 0; i < 10; i++) {
        m[i];
    }

    char* pc = static_cast<char*>(malloc(1024 * 1024));
    char* pc2 = new char[1024 * 1024];

    return 0;
}
