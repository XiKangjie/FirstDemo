#include "log.h"
using namespace Log;

void func1();
void func2();
void func3();
void func4();


void func1()
{
    CHECKPOINT("fun1 : %s\n" << "called.");
    func2();
}

void func2()
{
    CHECKPOINT("funr2 : %s\n" << "called.");
    func3();
    func4();
}

void func3()
{
    CHECKPOINT("fun3 : %s\n" << "called.");
    
    PUTLOG("error %s\n" << "func3");    
}

void func4()
{
    if(true) {
        PUTLOG("error %s\n" << "func4");    
        PrintCheckpoints();
    }
}

int main()
{
    CHECKPOINT("one : %f\n" << 1.1);
    {
        CHECKPOINT("two: %d\n" <<  2);
        {
            CHECKPOINT("three : %d\n" << 3);
            {
                PUTLOG("error\n");
                PrintCheckpoints();
            }
        }
    }

    func1();

    return 0;
}
