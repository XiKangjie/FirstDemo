#include <iostream>
#include <cstdio>
using namespace std;

int g = 100;

int& get_g()
{
    return g;
}

int main()
{
    int i = 0;

    i = 1;

    int *p = &i;

    *p = 2;

    printf("%d\n", i);
    printf("%d\n", *p);

    printf("addr: %p\n", &g);
    printf("addr: %p\n", &get_g());
    get_g() = 1000;
    printf("addr: %p\n", &get_g());

    return 0;
}
