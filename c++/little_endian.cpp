#include <iostream>
#include <cstdio>
using namespace std;

bool is_little_endian()
{
    int ax = 0x12345678;
    printf("ax value: 0x123345678\n");
    printf("ax addr: %p\n", &ax);
    printf("%x addr: %p\n", *(char*)&ax, (char*)&ax);
    printf("%x addr: %p\n", *((char*)&ax + 1), (char*)&ax + 1);
    printf("%x addr: %p\n", *((char*)&ax + 2), (char*)&ax + 2);
    printf("%x addr: %p\n", *((char*)&ax + 3), (char*)&ax + 3);
    int ah = *(char*)&ax;
    printf("ah value: 0x78\n");
    printf("ah addr: %p\n", &ah);
    printf("%x addr: %p\n", *(char*)&ah, (char*)&ah);
    printf("%x addr: %p\n", *((char*)&ah + 1), (char*)&ah + 1);
    printf("%x addr: %p\n", *((char*)&ah + 2), (char*)&ah + 2);
    printf("%x addr: %p\n", *((char*)&ah + 3), (char*)&ah + 3);
    if(ah == 0x78) {
        return true;
    }
    return false;
}

int main()
{
    if (is_little_endian()) {
        cout << "\nLittle Endian." << endl;
    }
    else {
        cout << "\nBig Endian." << endl;
    }

    return false;
}
