#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

#define FILENAME_LEN 64

static char* GetFileName()
{
    static char fname[FILENAME_LEN] = {0};
    static char fname_old[FILENAME_LEN] = {0};
    if (fname[0] == 0) {
        //snprintf(fname, FILENAME_LEN, "test%d.txt", getpid());
        snprintf(fname, FILENAME_LEN, "test.txt", getpid());
        snprintf(fname_old, FILENAME_LEN, "%s.old", fname);
        printf("init file name '%s' and '%s'\n", fname, fname_old);
    }
    struct stat st;
    stat(fname, &st);
    printf("sizeof(st_size): %lu\n", sizeof(st.st_size));   // 8
    printf("st_size: %lld\n", (long long)st.st_size);                  // 0
    if (st.st_size >= 8) {
        printf("rename %s to %s\n", fname, fname_old);
        rename(fname, fname_old);
    }
    if (access(fname, F_OK) == -1) {
        printf("create %s\n", fname);
        int fd = creat(fname, 0644);
        close(fd);
    }
    return fname;
}

int main()
{
    printf("first: %s\n", GetFileName());
    printf("second: %s\n", GetFileName());

    return 0;
}
