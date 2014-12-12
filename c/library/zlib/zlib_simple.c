#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zlib.h>

struct _Data{
    int size;
    char* str;
    struct _Data* next;
};
typedef struct _Data Data;

#define BUFFER_LEN 10000

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

    do {
        strm.avail_in = data->size;
        strm.next_in = data->str;
        flush = data->next ? Z_NO_FLUSH: Z_FINISH;
        data = data->next;

        do {
            strm.avail_out = BUFFER_LEN;
            strm.next_out = out;
            ret = deflate(&strm, flush);
            
            have = BUFFER_LEN - strm.avail_out;
            printf("have: %d\n", have);
            if (have > 0) {
                fwrite(out, 1, have, dest);
            }
        } while (strm.avail_out == 0);
    } while (flush != Z_FINISH);

/*
 *    while (data) {
 *        strm.avail_in = data->size;
 *        strm.next_in = data->str;
 *
 *
 *
 *        data = data->next;
 *    }
 */
    deflateEnd(&strm);
    return Z_OK;    
}

int main()
{
    Data d, d2;
    d.size = 64;
    d.str = (char*)malloc(64);
    memset(d.str, 'A', sizeof(char) * 64);
    d.next = NULL;

    d2.size = 128;
    d2.str = (char*)malloc(128);
    memset(d2.str, 'B', sizeof(char) * 128);
    d2.next = NULL;

    d.next = &d2;
    
    FILE* output = fopen("zlib_simple.z", "w");
    def(&d, output);

    return 0;
}
