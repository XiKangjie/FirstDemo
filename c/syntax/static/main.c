#include <stdio.h>
#include "foo.h"

int main()
{
    //foo();
    //foo2();     // warning: ‘foo2’ used but never defined
    //foo3();     // warning: ‘foo3’ used but never defined
    foo4();

    return 0;
}

/*

foo4
foo2
foo3

*/
