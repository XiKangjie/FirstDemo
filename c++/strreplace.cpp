#include <iostream>
//#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string str("abc, edf, asda, asdf");
    //replace(str.begin(), str.end(), ",", "nsfocus");
    size_t pos = 0;
    while((pos = str.find(',', pos)) != string::npos) {
        str.replace(pos, 1, "nsfocus");     // 1 == len(',')
        pos += 7;                           // 7 == len("nsfocus")
    }


    cout << str << endl;
    return 0;
}
