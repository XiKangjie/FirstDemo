#include <stdio.h>
#include <zlib.h>

int PlayBack(FILE* backup)
{
    Stream ss;
    while (true) {
        memset(&ss, ); 
        // header
        // dolog
        while (true) {
            // stream
            PushStream() 
        }
    }

    return 0;
}

int main(int argc, char** argv)
{
    int err_code;
    if ((err_code = CreateEngine()) != ERROR_NORMAL) {
        printf("%s\n", GetErrorMsg(err_code));
        return -1;
    }

    FILE* backup_file = fopen("1234.bak", "rb");
    PlayBack(backup_file);

    DestroyEngine();

    return 0;
}
