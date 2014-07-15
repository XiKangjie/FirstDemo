// test substr() with empty string
// test substr(pos, len), len > string.length()
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string empty;
    cout << empty.substr(0, 4) << endl; // no error, output null

    return 0;
}
