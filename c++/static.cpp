#include <iostream>
#include <stdio.h>
using namespace std;

int  Foo()
{
    static int i = 0;
    return ++i;
}

class Bar
{
public:
    static Bar b;
    int a;
};
Bar Bar::b = Bar();


class Init
{
public:
    int a;
    int b[4];
    char c[5];
};

int main()
{
    cout << Foo() << endl;
    cout << Foo() << endl;
    // cout << i << endl;

    Bar bar;
    bar.a = 1;
    printf("bar.a: %d\n", bar.a);
    bar.b.a = 2;
    printf("bar.a: %d\n", bar.a);
    printf("bar.b.a: %d\n", bar.b.a);
    bar.b.b.a = 3;
    printf("bar.a: %d\n", bar.a);
    printf("bar.b.a: %d\n", bar.b.a);
    printf("bar.b.b.a: %d\n", bar.b.b.a);

    static Init in;
    printf("\nin.a: %d\n", in.a);
    printf("in.b[0]: %d\n", in.b[0]);
    printf("in.c: %s\n", in.b);

    return 0;
}
