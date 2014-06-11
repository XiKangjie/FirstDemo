#include <iostream>
#include <pthread.h>
#include "timeuse.h"

int main()
{
    TimeUse tu;
    tu.Start();
    pthread_mutex_t lock;
    pthread_mutex_init(&lock, NULL);
    for (int i = 0; i < 1; i++) {
        pthread_mutex_lock(&lock);
        pthread_mutex_unlock(&lock);
    }
    pthread_mutex_destroy(&lock);
    tu.End();
    tu.PrintTimeUse();

    return 0;
}
