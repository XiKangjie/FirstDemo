#include <stdio.h>
#include <stddef.h>

typedef struct _Node {
    int a;
    long long b;
    char* c;
} Node;

typedef struct _Node2 {
    int a;
    long long b;
    char* c;
} __attribute__((packed)) Node2;

int main()
{
    printf("c offset: %lu\n", (unsigned long)(&( ((Node*)0)->c) ));     // 16
    printf("c offset: %lu\n", (unsigned long)(&( ((Node2*)0)->c) ));    // 12

    printf("c offset: %lu\n", offsetof(Node, c));     // 16
    printf("c offset: %lu\n", offsetof(Node2, c));    // 12

    return 0;
}
