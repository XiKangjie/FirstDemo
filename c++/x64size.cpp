#include <iostream>
#include <cstdio>
using namespace std;

void calc_size(long a[])
{
    cout << sizeof(a) << endl;
}

struct FOO
{
    const char* fmt;
    long array[5];
};

int main()
{
    printf("FOO size: %d\n", sizeof(FOO));  // 48;
    cout << sizeof(int) << endl;        // 4
    cout << sizeof(long) << endl;       // 8
    cout << sizeof(void *) << endl;     // 8
    const char* str = "abc";
    cout << sizeof(str) << endl;        // 8
    long la[4];
    cout << sizeof(la) << endl;         // 32
    calc_size(la);                      // 8
    long* ptrl = la;
    cout << sizeof(ptrl) << endl;       // 8
    printf("str : %x\n", str);          // 400a34
    printf("str addr: %p\n", &str);
    const char* str2 = str;
    printf("str2: %x\n", str2);         // 400a34
    printf("str2 addr: %p\n", &str2);

    int array[64];
    const int* ptr = array;
    cout << sizeof(ptr) << endl;        // 8
    printf("array addr: %p\n", &array[0]);
    printf("ptr addr: %p\n", ptr);      // 0x7fffc52c4710
    *((const char**)ptr) = str;
    printf("str addr: %p\n", str);      // 0x400a34
    printf("ptr addr: %p\n", ptr);      // 0x7fffc52c4710
    printf("ptr: %s\n", *ptr);          // abc
    printf("ptr[0]: %x\n", ptr[0]);     // 400a34
    printf("ptr[1]: %x\n", ptr[1]);     // 0
    printf("array[0]: %d, array[1]: %d\n", array[0], array[1]);

    int array2[4] = {0, 1, 2, 3};
    const int* ptr2 = array2;
    printf("ptr2: %p\n", ptr2);
    printf("array2 : %p\n", array2);
    printf("array2[0] addr: %p\n", &array2[0]);
    printf("array2[0]: %d, array2[1]: %d\n", array2[0], array2[1]);
    *((const char**)ptr2) = str;        // change the content that pointer point to.
                                        // ptr2原来是指针，现在变成了指向指针的指针。
    printf("array2[0]: %d, array2[1]: %d\n", array2[0], array2[1]);
    printf("(const char**)ptr2: %p\n", (const char**)ptr2);
    printf("ptr2 addr: %p\n", &ptr2);
    printf("ptr2: %p\n", ptr2);
    // (char*)ptr2 = str;               // error: lvalue required as left operand of assignment
    // printf("array2[0]: %d, array2[1]: %d\n", array2[0], array2[1]);


    return 0;
}
