#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main()
{
    unordered_multimap<int, string> name;
    typedef unordered_multimap<int, string>::iterator name_it;
    
    name.insert(make_pair(1, "xikangjie"));
    name.insert(make_pair(2, "chaihui"));
    name.insert(make_pair(1, "consen"));
    name.insert(make_pair(2, "xiaoshihui"));

    name_it it;
    for(it = name.begin(); it != name.end(); it++)
        cout << it->first << ": " << it->second << endl;
    cout << endl;

    it = name.find(1);
    for(; it != name.end(); it++)
    {
        if(it->second == "xikangjie")
            name.erase(it);
        cout << it->first << ": " << it->second << endl;
    }
    cout << endl;
    // output
    // 0:
    // 1: consen
    // 2: chahui
    // 2: xiaoshihui

    /*
    // has no member functions lower_bound() and upper_bound().
    name_it beg = name.lower_bound(2);
    name_it end = name.upper_bound(2);
    while(beg != end)
    {
        cout << it->second << endl;
        ++beg;
    }
    cout << endl;
    */

    pair<name_it, name_it> pos = name.equal_range(2);
    while(pos.first != pos.second)
    {
        cout << pos.first->second << endl;
        ++pos.first;
    }

    return 0;
}
