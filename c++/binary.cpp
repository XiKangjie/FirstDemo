#include <iostream>
using namespace std;

const unsigned int ID = 0b00000010000000100000000000000000;

int main()
{
    unsigned int a = 0b00000010000000111111111111111111;
    if ( a & ID) {
        cout << a << endl;
    }

    return 0;
}
