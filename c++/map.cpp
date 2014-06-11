#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<int, string> name;
    name[0] = "chaihui";
    name[1] = "xikangjie";

    map<int, string>::iterator it;
    for( it = name.begin(); it != name.end(); it++)
    {
        if(it->second == "chaihui")
            name.erase(it);
        cout << it->first << ": " << it->second << endl;
    }
    // output
    // 0:
    // 1: xikangjie

    return 0;
}
