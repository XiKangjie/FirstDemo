#include <iostream>
using namespace std;

const unsigned int PHONE = 3;

unsigned int get_type(unsigned int id)
{
    return (id >> 17) & 0x7F;
}

int main()
{
    cout << get_type(33947649) << endl;
    cout << get_type(33816578) << endl;
    cout << get_type(33685504) << endl;
    cout << get_type(33685503) << endl;

    return 0;
}
