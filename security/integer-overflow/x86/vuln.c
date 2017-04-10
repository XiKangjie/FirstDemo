//vuln.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void store_passwd_indb(char* passwd) {  }

void validate_uname(char* uname) {  }

void validate_passwd(char* passwd)
{
    char passwd_buf[11];
    printf("%p\n", passwd_buf);
    unsigned char passwd_len = strlen(passwd);
    if (passwd_len >= 4 && passwd_len <= 8) {
        printf("Valid Password\n");
        strcpy(passwd_buf,passwd);
    } else {
        printf("Invalid Password\n");
    }
    store_passwd_indb(passwd_buf);
}

int main(int argc, char* argv[])
{
    if (argc!=3) {
        printf("Usage Error.\n");
        exit(-1);
    }

    setuid(0);

    validate_uname(argv[1]);
    validate_passwd(argv[2]);

    return 0;
}

