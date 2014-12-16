#include <stdio.h>
#include "foo.h"

// static declaration of ‘foo’ follows non-static declaration
/*
static void foo()
{
    printf("foo\n");
}
*/

void foo2()
{
    printf("foo2\n");
}

static void foo3()
{
    printf("foo3\n");
}

void foo4()
{
    printf("foo4\n");
    foo2();
    foo3();
}
