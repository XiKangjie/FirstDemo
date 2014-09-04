#include <iostream>
#include <typeinfo>
#include <hash_map>
#include <string>
using namespace std;

struct Foo
{
    int bar;
};

typedef hash_map<int, Foo> tFoo;

int main()
{
    hash_map<string, int> type_num;
    
    cout << "int is: " << typeid(int).name() << endl;
    cout << "double is: " << typeid(double).name() << endl;
    cout << "char is: " << typeid(char).name() << endl;
    cout << "string is: " << typeid(string).name() << endl;
    cout << "Foo is: " << typeid(Foo).name() << endl;
    cout << "tFoo is: " << typeid(tFoo).name() << endl;

    type_num[typeid(int).name()] = 1;
    type_num[typeid(double).name()] = 1;
    type_num[typeid(char).name()] = 1;
    type_num[typeid(string).name()] = 1;
    type_num[typeid(Foo).name()] = 1;
    type_num[typeid(tFoo).name()]++;

    hash_map<string, int>::iterator it;
    for (it = type_num.begin(); it != type_num.end(); it++) {
        cout << it->first << " : " << it->second << endl;
    }

    return 0;
}

// int is: i
// double is: d
// char is: c
// string is: N8stlp_std12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
// Foo is: 3Foo
// tFoo is: N8stlp_std8hash_mapIi3FooNS_4hashIiEENS_8equal_toIiEENS_9allocatorINS_4pairIKiS1_EEEEEE
// i : 1
// c : 1
// d : 1
// N8stlp_std12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 1
// N8stlp_std8hash_mapIi3FooNS_4hashIiEENS_8equal_toIiEENS_9allocatorINS_4pairIKiS1_EEEEEE : 1
// 3Foo : 1
