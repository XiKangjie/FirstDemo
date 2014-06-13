#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> v;
    cout << "size: " << sizeof(v) << endl;      // 24
    for (int i = 0; i < 10; i++) {
        v.push_back(i);
    }
    cout << "size: " << sizeof(v) << endl;      // 24

    if(!v.empty())
        cout << v.at(0) << endl;

    v.push_back(20);
    v.push_back(30);

    vector<int>::iterator it;
    for(it = v.begin(); it != v.end();)
    {
        if(*it == 1)
        {
            cout << "erase 1" << endl;
            it = v.erase(it);
        }
        else
            cout << *(it++) << endl;
    }

    return 0;
}
