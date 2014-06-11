#ifndef TIME_USE_H
#define TIME_USE_H

#include <stdio.h>
#include <sys/time.h>

class TimeUse
{
public:
    void Start() {
        gettimeofday(&start, NULL);
        printf("start.sec: %u, start.usec: %u\n", (unsigned int)start.tv_sec, (unsigned int)start.tv_usec);
    }  
    void End() {
        gettimeofday(&end, NULL);
        printf("end.sec: %u, end.usec: %u\n", (unsigned int)end.tv_sec, (unsigned int)end.tv_usec);
    }  
    void PrintTimeUse() {
        int timeuse = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
        printf("timeuse: %d us\n", timeuse);
    }  
private:
    struct timeval start;
    struct timeval end;
};

#endif
