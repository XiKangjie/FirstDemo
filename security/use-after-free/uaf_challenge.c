#include <stdio.h>
#include <string.h>

int main() {
    char** chunks[2];
    char* buf = "ABCD";

    chunks[0] = malloc(8);
    memcpy(chunks[0], buf, 8);

    printf("%s\n", chunks[0]);
    //printf("%s\n", *chunks[0]);

    return 0;
}
