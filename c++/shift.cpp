#include <iostream>
using namespace std;

int main()
{
    int i = 1;
    cout << "i: "<< i << endl;
    i <<= 0;
    cout << "i << 0: " << i << endl;
    i <<= 1;
    cout << "i << 1: " << i << endl;

    return 0;
}
