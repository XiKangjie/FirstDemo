#include <iostream>
using namespace std;

int main()
{
    /*
    const int ci = 1;
    const int* cp = &ci;
    int* p = const_cast<int*>(cp);
    *p = 0;

    cout << *cp << endl;    // 0
    cout << *p << endl;     // 0
    cout << ci << endl;     // 1

    const int& cr = ci;
    int& r = const_cast<int&>(cr);
    r = 2;

    cout << cr << endl;     // 2
    cout << r << endl;      // 2
    cout << ci << endl;     // 1
    */
    
    int i = 1;
    const int* cp = &i;
    int* p = const_cast<int*>(cp);
    *p = 0;

    cout << *cp << endl;    // 0
    cout << *p << endl;     // 0
    cout << i << endl;      // 0

    const int& cr = i;
    int& r = const_cast<int&>(cr);
    r = 2;

    cout << cr << endl;     // 2
    cout << r << endl;      // 2
    cout << i << endl;      // 2

    return 0;
}
