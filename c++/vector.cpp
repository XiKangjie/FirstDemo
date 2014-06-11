#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> v;
    v.push_back(1);

    if(!v.empty())
        cout << v.at(0) << endl;

    v.push_back(20);
    v.push_back(30);

    vector<int>::iterator it;
    for(it = v.begin(); it != v.end(); it++)
    {
        if(*it == 1)
        {
            cout << "erase 1" << endl;
            v.erase(it);
        }
        else
            cout << *it << endl;
    }
    // output
    // 1
    // erase 1
    // 30

    return 0;
}
