#include <iostream>
#include <list>
using namespace std;

int main()
{
    list<int> myints;
    cout << "0. size: " << myints.size() << endl;
    
    for (int i = 0; i < 10; i++) {
        myints.push_back(i);
        int listsize = myints.size();
        cout << "1. size: " << listsize << endl;
    }

    myints.clear();
    if (myints.empty()) {       // more efficient than myints.size() == 0
        cout << "2. size: " << myints.size() << endl;
    }

    return 0;
}
