// -I /usr/include/stlport -lstlport
#include <iostream>
#include <hash_map>
using namespace std;

int main()
{
    hash_map<int, int> m(1024);
    cout << m.size() << endl;   // 0
    cout << m.bucket_count() << endl;   // 1543
    cout << sizeof(m) << endl;
    
    hash_map<int, int> e;
    cout << e.bucket_count() << endl;
    cout << sizeof(e) << endl;

    return 0;
}
