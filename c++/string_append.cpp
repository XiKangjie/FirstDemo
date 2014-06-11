#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str("Hello world");
    cout << str << endl;
    str.append("!");
    cout << str << endl;

    string s("abc");
    s = "," + s + ",";
    cout << s << endl;

    return 0;
}
