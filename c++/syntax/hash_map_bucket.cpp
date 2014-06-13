#include <iostream>
#include <hash_map>
using namespace std;

int main()
{
    std::hash_map<int, int> m;
    cout << "bucket_count: " << m.bucket_count() << endl;

    for (int i = 1; i <= 4; i++) {
        m[i] = i;
    }
    cout << "bucket_count: " << m.bucket_count() << endl;
    cout << "size: " << sizeof(m) << endl;      // 56
    m.clear();
    cout << "size: " << sizeof(m) << endl;      // 56
    
    for (int i = 5; i <= 70; i++) {
        m[i] = i;
    }
    cout << "bucket_count: " << m.bucket_count() << endl;
    cout << "size: " << sizeof(m) << endl;      // 56
    m.clear();
    cout << "size: " << sizeof(m) << endl;      // 56

    hash_multimap<int, int> mm;
    typedef hash_multimap<int, int>::value_type VALUE;
    mm.insert(VALUE(1, 101));
    mm.insert(VALUE(1, 102));
    mm.insert(VALUE(1, 103));
    mm.insert(VALUE(1, 104));
    
    int n = mm.bucket_count();
    cout << "buckets: " << n << endl;

    typedef hash_multimap<int, int>::iterator IT;
    /*
    for (int i = 0; i < n; i++)
    {
        cout << "bucket " << i << " ";
        for (IT it = mm.begin(i); it != mm.end(i); it++)
        {
            cout << it->first << ":" << it->second;
        }
        cout << endl;
    }
    */

    for (IT it = mm.begin(); it != mm.end(); it++)
    {
        cout << it->second << endl;
    }
    cout << "2 counts: " << mm.count(1) << endl;
    pair<IT, IT> bounds;
    bounds = mm.equal_range(1);
    for (IT it = bounds.first; it != bounds.second; it++) {
        cout << it->second << endl;
    }

    return 0;
}
