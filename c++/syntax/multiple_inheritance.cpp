#include <iostream>
using namespace std;

class BaseA
{
public:
    BaseA(int i): a(i) {}
    virtual ~BaseA() {}

    void fa() {
        cout << "BaseA " << a << endl;
    }

private:
    int a;
};

class BaseB
{
public:
    BaseB(int i): b(i) {}
    virtual ~BaseB() {}

    void fb() {
        cout << "BaseB " << b << endl;
    }

private:
    int b;
};

class Derived: public BaseA, public BaseB
{
public:
    Derived(int a, int b, int i): BaseA(a), BaseB(b), c(i) {}

    void fd() {
        cout << "Derived " << c << endl;
    }

private:
    int c;
};

int main()
{   
    // pointer to virtual table
    // {<BaseA> = {_vptr.BaseA = 0x4010b0, a = 1}, <BaseB> = {_vptr.BaseB = 0x4010d0, b = 2}, c = 3}
    Derived d(1, 2, 3);
    Derived* pd = &d;
    cout << "pd address: " << pd << endl;

    void* pv = pd;
    cout << "pv address: " << pv << endl;

    BaseA* pa = pd;
    cout << "pa address: " << pa << endl;
    pa->fa();

    BaseB* pb = pd;     //@ pb point to BaseB section.
    cout << "pb address: " << pb << endl;
    pb->fb();

    // Derived* pdd = pa;   // error: invalid conversion from ‘BaseA*’ to ‘Derived*’
    Derived* pdd = dynamic_cast<Derived*>(pa);
    cout << "pdd address: "<< pdd << endl;
    pdd->fd();

    return 0;
}

/*

pd address: 0x7fffa232ed90
pv address: 0x7fffa232ed90
pa address: 0x7fffa232ed90
BaseA 1
pb address: 0x7fffa232eda0
BaseB 2
pdd address: 0x7fffa232ed90
Derived 3

*/
