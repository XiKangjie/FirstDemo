// test variable scope when use goto. 

#include <iostream>
using namespace std;

int main()
{
    int x = 100;
    {
        int x = 200;
        goto error;
    }

error:
    cout << x << endl;      // 100

    return 0;
}
