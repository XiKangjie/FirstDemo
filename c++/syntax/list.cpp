#include <iostream>
#include <list>
using namespace std;

int main()
{
    list<int> myints;
    cout << "0. size: " << myints.size() << endl;
    
    for (int i = 0; i < 10; i++) {
        myints.push_back(i);
        cout << "1. size: " << myints.size() << endl;
    }

    myints.clear();
    cout << "3. size: " << myints.size() << endl;

    return 0;
}
