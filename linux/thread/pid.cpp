#include <stdio.h>
#include <pthread.h>
#include "../timeuse.h"

int main()
{
    TimeUse tu;
    tu.Start();
    pthread_t tid;
    for (int i = 0; i < 10000; i++) {
         tid = pthread_self();
    }
    tu.End();
    tu.PrintTimeUse();

    printf("%u\n", (unsigned int)(tid));

    return 0;
}
