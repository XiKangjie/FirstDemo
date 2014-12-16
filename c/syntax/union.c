#include <stdio.h>
#include <stdint.h>

typedef union
{
    union
    {
        struct { uint8_t s1, s2, s3, s4; } b;
        struct { uint16_t s1, s2; } w;
        struct { uint32_t s; } dw;
    } v4;
    struct 
    {
        uint32_t to_v4_s;
        union
        {
            struct { uint8_t s[16]; } b;
            struct { uint16_t s[8]; } w;
            struct { uint32_t s1, s2, s3, s4; } dw;
            struct { uint64_t s1, s2; } ll;
        } s;
    } v6;
} __attribute__((packed)) Ip;


typedef struct {
    uint32_t ipv6;
    // anonymous union
    union {
        uint32_t v4addr;
        struct { uint64_t v6addr1, v6addr2; };
    };
} __attribute__((packed)) ipaddr;

int main()
{
    Ip ip = { .v4.dw.s = 0x12345678 };
    printf("%x\n", ip.v4.dw.s);
    printf("%x, %x\n", ip.v4.w.s1, ip.v4.w.s2);
    printf("%x, %x, %x, %x\n", ip.v4.b.s1, ip.v4.b.s2, ip.v4.b.s3, ip.v4.b.s4);

    printf("%x\n", ip.v6.s.dw.s1);
    printf("%x\n", ip.v6.to_v4_s);


    ipaddr addr;
    addr.ipv6 = 1;
    addr.v6addr1 = 0x1234567812345678;
    addr.v6addr2 = 0x8765432187654321;
    printf("%lx\n", addr.v6addr1);
    printf("%lu\n", sizeof(addr));      // 20

    ipaddr addr2;
    addr2.ipv6 = 0;
    addr2.v4addr = 0x12345678;
    printf("%lu\n", sizeof(addr2));     // 20

    return 0;
}

/*

12345678
5678, 1234
78, 56, 34, 12
0
12345678
1234567812345678
20
20

*/
