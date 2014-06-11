#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int i = 10;
    printf("%p\n", &i);
    //printf("%x\n", &i);

    int& ri = i;
    printf("%p\n", &ri);
    //printf("%x\n", &ri);
    
    int* pi = &i;
    printf("%p\n", pi);
    printf("%p\n", &pi);


    return 0;
}
