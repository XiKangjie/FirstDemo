#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<int, string> name;
    name[1] = "xikangjie";
    name[2] = "consen";

    map<int, string>::iterator it;
    for (it = name.begin(); it != name.end(); it++) {
        cout << it->second << endl;
    }

    name.erase(1);
    name.erase(1);

    for (it = name.begin(); it != name.end(); it++) {
        cout << it->second << endl;
    }

    return 0;
}
