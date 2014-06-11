#include <iostream>
#include <set>
#include <string>
using namespace std;

int main()
{
    set<string*> ssp;
    ssp.insert(new string("consen"));
    ssp.insert(new string("xi"));
    ssp.insert(new string("chai"));

    set<string*>::iterator it;
    for (it = ssp.begin(); it != ssp.end(); it++)
    {
        cout << *it << endl;
        cout << **it << endl;
    }

    return 0;
}
