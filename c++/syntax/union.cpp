#include <iostream>
using namespace std;

union S
{
    unsigned int n;
    unsigned short int s[2];
    unsigned char c;
};

int main()
{
    S s = { 0x12345678 };
    cout << hex << "s.n = " << s.n << endl;
    s.s[0] = 0x0011;
    cout << "s.c is now " << +s.c << endl
         << "s.n is now " << s.n << endl;

    return 0;
}

/*

s.n = 12345678
s.c is now 11
s.n is now 12340011

*/
