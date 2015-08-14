#include <stdio.h>

#ifndef PRINT
#define PRINT
#endif

int main()
{
// still can be tested
#ifdef PRINT
    printf("hello %d\n", PRINT 100);
#endif

    return 0;
}

/*

hello 100

*/
