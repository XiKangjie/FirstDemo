#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main()
{
    int num;
    string str = "";
    num = static_cast<int>(strtoul(str.c_str(), NULL, 10));

    cout << num << endl; // 0

    return 0;
}
