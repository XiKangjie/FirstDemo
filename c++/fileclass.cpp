#include <iostream>
#include <cstdio>
#include <cstring>
#include <unistd.h>
using namespace std;


class File
{
public:
    void Write(const char* str);

    File() {
        fd = fopen("./fileclass.txt", "a");
    }
    ~File() {
        fclose(fd);
    }

private:
    FILE* fd;
};

void File::Write(const char* str)
{
    fwrite(str, sizeof(char), strlen(str), fd);
    //cout << str << endl;
    //cout << sizeof(char) << endl;
    //cout << strlen(str) << endl;
    fflush(fd);
}

int main()
{
    File f;
    while (true) {
        f.Write("this is test.\n");
        sleep(2);
    }

    return 0;
}
