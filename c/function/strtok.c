#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

int main()
{
    unsigned long ul;
    printf("sizeof unsigned long: %lu\n", sizeof(unsigned long));

    char str0[] = "123,456, 789";
    char str2[] = "123";
    char str[] = "4294967295";
    char* pch;
    int len = strlen(str);
    printf("Splitting string \"%s\" into tokens:\n", str);
    pch = strtok(str, ",");
    while (pch != NULL) {
        printf("token:%s\n", pch);
        ul = strtoul(pch, NULL, 10);
        uint32_t ui = ul;
        printf("ul:%lu\n", ul);
        printf("ui:%u\n", ui);
        pch = strtok(NULL, ",");
    }
    printf("After strtok(), the string is:\n");
    int i = 0;
    for (i = 0; i < len; i++) {
        if (str[i] == '\0') {
            printf("\\0");
        }
        else {
            printf("%c", str[i]);
        }
    }
    printf("\n");

    return 0;
}
