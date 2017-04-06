/* 
 * Compile, disable stack canaries and NX: gcc -fno-stack-protector -z execstack vulnerability.c -o vulnerability
 * Disable ASLR: echo 0 > /proc/sys/kernel/randomize_va_space 
 *
 * sudo chown root:root vulnerability
 * sudo chmod +s vulnerability
*/
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    setuid(0);

    char buf[256];

    printf("%p\n", buf);
    strcpy(buf, argv[1]);
    printf("%s\n", buf);

    return 0;
}
