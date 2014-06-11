#include <iostream>
#include <string>
#include <hash_map>
using namespace std;

namespace nsfocus {

typedef hash_map<int, string> NameTable;
NameTable MakeNameTable() {
    NameTable table;
    table[1] = "xikangjie";
    return table;
}

NameTable table = MakeNameTable();

}

int g = 10;

struct Foo
{
    int a;
    Foo(): a(1) {}
};

int main()
{
    cout << g << endl;

    hash_map<int, string> name;
    name[0] = "consen";
    cout << name[0] << endl;
    
    //nsfocus::nametable.insert(make_pair(1, "xikangjie"));
    cout << nsfocus::table[1] << endl;


    hash_map<int, Foo> f;
    cout << f[0].a << endl;

    return 0;
}
