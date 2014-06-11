#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int a = 10;
    int* p = &a;
    cout << p << "     " << *p << endl;
    
    //*((int**)p) = 11;       // invalid conversion from ‘int’ to ‘int*’
    *p = 11;
    cout << p << "     " << *p << endl;
    
    int b = 20;
    int *pb = &b;
    int **ppb = &pb;
    // (int**)p = ppb;           // lvalue required as left operand of assignment
    // cout << *p << "    " << **p << endl;

    char str[4] = {'a', 'b', 'c', 0};
    cout << str << endl;
    // char** pps = &str;          // cannot convert ‘char (*)[4]’ to ‘char**’ in initialization
    // cout << *pps << endl;
    cout << str << endl;


    void* vp = 0;
    vp = &b;
    // (int*)vp = &a;  // error: lvalue required as left operand of assignment
    *((int**)vp) = &a;  // ok
    pb = (int*)vp;     // ok
    vp = &a;

    //char* cp = vp;  // error: invalid conversion from ‘void*’ to ‘char*’
    //char* cp = (char*)vp; // ok
    char* cp = *((char**)vp);   // ok

    short int si = 100;
    // (int)si = 101;  // error: lvalue required as left operand of assignment
    // (int)si是临时值，非左值，不能用于做操作数
    //
    int array[64];
    char* cstr = "abc";
    /*
    int* ap = array;
    cout << ap << endl;
    *((char**)ap) = cstr;
    */
    *((char**)(array + 1)) = cstr;                // 是怎样将数组第一个元素内容改成cstr的？？ array + 1是一个char*
    cout << array[1] << endl;
    cout << (char*)(array[1]) << endl;      // abc

    *((int**)(array + 2)) = pb;             // array + 2现在是一个int*
    //cout << array[2] << endl;
    printf("array[2]: %x\n", array[2]);     // array[2] 和 array[3] 中存放pb, 即b的地址。
    printf("array[3]: %x\n", array[3]);
    cout << &b << endl;
    
    int* p4 = array + 4;
    *((int*)p4) = 4;
    cout << array[4] << endl;   // 4

    //array + 5 = p;              // error: lvalue required as left operand of assignment
    //printf("array[5]: %x\n", array[5]);
    //printf("array[6]: %x\n", array[6]);

    int* p10 = array + 10;
    *((long*)p10) = 11111111111111111;
    printf("long: %ld\n", *((long*)p10));
    printf("long: %ld\n", *((long*)(array + 10)));

    int* p12 = array + 12;
    *((double*)p12) = 1111111111.111;
    printf("double: %f\n", *((double*)p12));
    printf("double: %f\n", *((double*)(array + 12)));
    return 0;
}            
