#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int a = 1;
    int* pa = &a;

    cout << pa << endl;
    //cout << int(pa) << endl;
    cout << sizeof(int) << endl;    //4
    printf("%ld\n", sizeof(int));   //4
    cout << sizeof(long) << endl;   //8
    printf("%ld\n", sizeof(long));  //8
    cout << sizeof(int*) << endl;   //8
    printf("%ld\n", sizeof(int*));  //8
    cout << sizeof(void*) << endl;  //8

    int b = 1;
    int* pb = &b;
    if(pa == pb)
        cout << "same" << endl;
    else
        cout << "diff" << endl;

    return 0;
}
