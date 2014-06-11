#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    FILE* pf = fopen("/dev/pts/4", "a");
    fprintf(pf, "\ntest\n");
    fclose(pf);

    return 0;
}
