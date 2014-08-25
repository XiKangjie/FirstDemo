#include <iostream>
#include <cstdio>
using namespace std;

#define RAND_2(x, y) x##y
#define RAND_1(x, y) RAND_2(x, y)
#define RAND(prefix) RAND_1(prefix, __LINE__)

int main()
{
    RAND(recAutoToLog);
    RAND(var##_Record);

    return 0;
}
