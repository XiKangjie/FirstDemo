//
// clear() doesn't clear content.
//
#include <iostream>
#include <sstream>
using namespace std;

int main()
{
    stringstream stream;
    stream << "hello;";
    cout << stream.str() << endl;   // hello;
    stream.clear();                 // clear() set 'error state flags' to goodbit(No errors),
                                    // doesn't clear content.
    stream << "world;";             // hello;world;
    cout << stream.str() << endl;

    stream.str("");                 // clear content.
    cout << stream.str() << endl;   // output empty.

    return 0;
}
