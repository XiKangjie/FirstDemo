#include <sys/time.h>
#include <stdio.h>
#include <string.h>


class TimeUse
{
public:
    void Start() {
        gettimeofday(&start, NULL);
    }
    void End() {
        gettimeofday(&end, NULL);
    }
    void PrintTimeUse() {
        int timeuse = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
        printf("timeuse: %d us\n", timeuse);
    }
private:
    struct timeval start, end;
};

void NoBuffer()
{
    FILE* fd = fopen("./writefile.txt", "a");
    for (int i = 0; i < 10000; i++) {
        fprintf(fd, "this is test%d.\n", 1);                             // 2400 us
        fflush(fd);
        //fclose(fd);
    }
    fclose(fd);
    //fflush(fd);
}

const int BUF_LEN = 160000;
char buf[BUF_LEN];
void UseBuffer()
{
    FILE* fd = fopen("./writefile.txt", "a");
    int n = 0;
    int len = 0;
    for (int i = 0; i < 10000; i++) {
        n = snprintf(buf + len, BUF_LEN - len, "this is test%d.\n", 2);
        len += n;
    }
    fwrite(buf, sizeof(char), len, fd);      // 20000 us(buffer) -> 400us (pbuf) -> 200us(+13) -> 1250us -> 2694us(1)
    //fflush(fd);
    fclose(fd);
}

int main()
{
    /*
    const char* str = "this is test%d.";
    char strbuf[16];
    char buffer[16 * 10000];
    char* pbuf = buffer;
       //snprintf(strbuf, 16, str, 1);
       ////fwrite(str, sizeof(char), strlen(str), fd);      // 2200 us
       //strcat(pbuf, strbuf);
       //pbuf += strlen(strbuf);
       //pbuf += 13;
    }
    ////fprintf(fd, str);                              // 18000 us
    //fwrite(buffer, sizeof(char), strlen(buffer), fd);      // 20000 us(buffer) -> 400us (pbuf) -> 200us(+13) -> 1250us -> 2694us(1)
    ////fputs(buffer, fd);  // 1750 us
    //fflush(fd);
    //fclose(fd);

    */

    
    TimeUse tu;
    
    tu.Start();
    NoBuffer();
    tu.End();
    tu.PrintTimeUse();

    tu.Start();
    UseBuffer();
    tu.End();
    tu.PrintTimeUse();

    return 0;
}
