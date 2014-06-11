#include <iostream>
#include <cstring>
#include <malloc.h>
using namespace std;

int main()
{
    char* str = (char*)malloc(512);

    for (int i = 0; i < 512; i++)
        cout << (int)str[i];
    cout << endl;

    strcat(str, "these ");
    strcat(str, "strings ");
    strcat(str, "are ");
    strcat(str, "concatenated.");
    
    cout << strlen(str) << endl;
    cout << str << endl;

    return 0;
}
