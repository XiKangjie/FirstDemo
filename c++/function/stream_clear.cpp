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

    string str;
    stream >> str;                  // >> reaches the end of the string and sets the eof bit.
    stream.str("");                 // clear content.
    stream.clear();                 // must reset stream state, otherwise can't <<.
    cout << stream.str() << endl;   // output empty.

    stream << "hello ?";            // hello ?
    cout << stream.str() << endl;

    return 0;
}
