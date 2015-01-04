#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv)
{
    int aflag = 0;
    char* fname = NULL;
    int opt = 0;
   
    /*
     * If an option was successfully found, then getopt() returns the option
     * character. If all command-line options have been parsed, then getopt()
     * returns -1. If getopt() encounters an option character that was not in
     * optstring, then '?' is returned.
     *
     * optstring, if such a character is followed by a colon, the option requires
     * an argument, two colons mean an option takes an optional arg. 
     */ 
    while ((opt = getopt(argc, argv, "af:h")) != -1) {
        switch (opt) {
            case 'a':
                aflag = 1;
                break;
            case 'f':
                fname = optarg;
                break;
            case 'h':
            case '?':
                printf("usage: ./getopt.exe [-a] -f filename\n");
        }
    }

    printf("aflag: %d\n", aflag);
    printf("fname: %s\n", fname);

    return 0;
}

/*

$ ./getopt.exe -a -f stat.c
aflag: 1
fname: stat.c

$ ./getopt.exe -a -fstat.c
aflag: 1
fname: stat.c

$ ./getopt.exe -a -f
./getopt.exe: option requires an argument -- 'f'
usage: ./getopt.exe [-a] -f filename
aflag: 1
fname: (null)

$ ./getopt.exe -f stat.c
aflag: 0
fname: stat.c

$ ./getopt.exe
aflag: 0
fname: (null)

$ ./getopt.exe -b
./getopt.exe: invalid option -- 'b'
usage: ./getopt.exe [-a] -f filename
aflag: 0
fname: (null)

*/
