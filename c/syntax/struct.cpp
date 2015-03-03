#include <iostream>
using namespace std;

struct Demo {};

int main()
{
    Demo d, d2;
    cout << "size of empty struct d: " << sizeof(d) << endl;
    cout << "addr of empty struct d:  " << &d << endl;
    cout << "addr of empty struct d2: " << &d << endl;

    return 0;
}

/*

size of empty struct d: 1
addr of empty struct d:  0x7fff383bbb7f
addr of empty struct d2: 0x7fff383bbb7f

*/
