#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zlib.h>

struct _Data{
    struct _Data* next;
    char* str;
    int size;
} __attribute__((packed));
typedef struct _Data Data;

#define BUFFER_LEN 100

int def(Data* data, FILE* dest)
{
    int ret, flush;
    unsigned have;
    z_stream strm;
    unsigned char out[BUFFER_LEN];

    strm.zalloc = Z_NULL;
    strm.zfree = Z_NULL;
    strm.opaque = Z_NULL;
    ret = deflateInit(&strm, Z_DEFAULT_COMPRESSION);
    if (ret != Z_OK) {
        return ret;
    }

    strm.avail_out = BUFFER_LEN;
    strm.next_out = out;

    do {
        strm.avail_in = data->size + sizeof(int);
        strm.next_in = (char*)data + sizeof(Data*) + sizeof(char*);
        printf("next_in: %p\n", strm.next_in);
        flush = data->next ? Z_NO_FLUSH: Z_FINISH;
        data = data->next;

        do {
            if (strm.avail_out == 0) {
                have = BUFFER_LEN - strm.avail_out;
                printf("have: %d\n", have);
                fwrite(out, 1, have, dest);
                strm.avail_out = BUFFER_LEN;
                strm.next_out = out;
            }
            ret = deflate(&strm, flush);
            
        } while (strm.avail_out == 0);
    } while (flush != Z_FINISH);

    have = BUFFER_LEN - strm.avail_out;
    fwrite(out, 1, have, dest);

    deflateEnd(&strm);
    return Z_OK;    
}

void free_data(Data* d)
{
    while (d) {
        Data* next = d->next;
        free(d);
        d = next;
    }
}

int main()
{
    void* buffer = malloc(sizeof(Data) + 4);
    Data* d = (Data*)buffer;
    d->next = NULL;
    d->str = (char*)d + sizeof(Data);
    printf("d->str: %p\n", d->str);
    d->size = 4;
    memset(d->str, 'A', sizeof(char) * 4);

    buffer = malloc(sizeof(Data) + 8);
    Data* d2 = (Data*)buffer;
    d2->next = NULL;
    d2->str = (char*)d2 + sizeof(Data);
    printf("d2->str: %p\n", d2->str);
    d2->size = 8;
    memset(d2->str, 'B', sizeof(char) * 8);

    d->next = d2;
    
    FILE* output = fopen("zlib_simple.z", "w");
    def(d, output);

    free_data(d);

    return 0;
}
