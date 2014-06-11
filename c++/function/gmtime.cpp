#include <stdio.h>
#include <time.h>
#include "../timeuse.h"

int main()
{

    TimeUse tu0;
    tu0.Start();
    tu0.End();
    tu0.PrintTimeUse();

    char buf[256];

    TimeUse tu2;
    tu2.Start();
    for (int i = 0; i < 10000; i++) {
        struct timeval tv;
        gettimeofday(&tv, NULL);
        struct tm* ptm2;
        ptm2 = localtime(&(tv.tv_sec));
        strftime(buf, 128, "%Y-%m-%d %H:%M:%S", ptm2);
    }
    tu2.End();
    printf("localtime(), ");
    tu2.PrintTimeUse();
    printf(buf);
    printf("\n");

    TimeUse tu;
    time_t t = time(NULL);
    tu.Start();
    for (int i = 0; i < 10000; i++) {
        struct tm* ptm;
        ptm = gmtime(&t);
        snprintf(buf, 256, "%04u-%02u-%02u %02u:%02u:%02u",
                ptm->tm_year + 1900, ptm->tm_mon + 1, ptm->tm_mday,
                (ptm->tm_hour + 8) % 24, ptm->tm_min, ptm->tm_sec);
    }
    tu.End();
    printf("gmtime(), ");
    tu.PrintTimeUse();
    printf(buf);
    printf("\n");


    return 0;
}
