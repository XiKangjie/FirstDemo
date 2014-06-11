#include <iostream>
#include <map>
#include <string>
using namespace std;

typedef map<int, string> MyMap;
MyMap createmap()
{
    MyMap ret;
    ret[1] = "xi";
    return ret;
}

const MyMap name = createmap();

//const MyMap table = {
//    MyMap::value_type(1, "consen")
//};

int main()
{
    if(name.find(1) != name.end())
        cout << "find" << endl;

    //cout << name.at(1) << endl;

    return 0;
}
