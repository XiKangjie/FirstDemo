#include "logger.h"

void functionnnn1();
void func2();
void func3();
void func4();

void functionnnn1()
{
    CHECKPOINT("checkpoint func1 " << 1232341234234);
    func2();
}

void func2()
{
    CHECKPOINT("checkpoint func2 " << 123.234);
    func3();
    func4();
}

void func3()
{
    CHECKPOINT("checkpoint func3" << 'a');
}

void func4()
{
    OUTPUTLOG("error in func4");
    PRINTCHECKPOINTS();
}

int main()
{
    CHECKPOINT("checkpoint " << 1);
    {
        CHECKPOINT("checkpoint " << 2);
        {
            OUTPUTLOG("error");
            PRINTCHECKPOINTS();
        }
    }

    functionnnn1();
    
    return 0;
}
