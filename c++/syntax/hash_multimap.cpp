#include <iostream>
#include <hash_map>
#include <string>
using namespace std;

int main()
{
    hash_multimap<int, string> name;
    typedef hash_multimap<int, string>::iterator name_it;

    name.insert(make_pair(1, "windows 8"));
    name.insert(make_pair(2, "ubuntu"));
    name.insert(make_pair(1, "windows 7"));
    name.insert(make_pair(3, "mac"));
    name.insert(make_pair(1, "windows xp"));
    name.insert(make_pair(2, "redhat"));
    name.insert(make_pair(3, "iphone"));
    name.insert(make_pair(3, "ipad"));
    name.insert(make_pair(2, "arch"));
    name.insert(make_pair(2, "gentoo"));

    name_it it = name.find(2);
    for(; it != name.end(); it++)
        cout << it->second << endl;
    cout << endl;

    pair<name_it, name_it> pos = name.equal_range(2);
    while(pos.first != pos.second)
    {
        cout << pos.first->second << endl;
        ++pos.first;
    }

    cout << endl << endl;

    it = name.find(2);
    for(; it != name.end(); it++)
    {
        cout << it->second << endl;
        if(it->second == "gentoo")
        {
            cout << "delete gentoo" << endl;
            name.erase(it);
        }
    }
    cout << endl;

    pos = name.equal_range(2);
    while(pos.first != pos.second)
    {
        cout << pos.first->second << endl;
        if(pos.first->second == "gentoo")
        {
            cout << "delete gentoo" << endl;
            name.erase(pos.first);
            break;
        }
        ++pos.first;
    }

    cout << endl;

    pos = name.equal_range(2);
    while(pos.first != pos.second)
    {
        cout << pos.first->second << endl;
        ++pos.first;
    }
    return 0;
}
