#include <stdio.h>
#include <zlib.h>

#define STREAM_HEADER_LEN (sieof(Stream) - sizeof(char*))
#define DOLOGID_COUNT_MAX 100


static Stream sss;

static int InputStreamHeader(Stream* ss, FILE* input_file)
{
    char header[STREAM_HEADER_LEN];
    fread(header, 1, STREAM_HEADER_LEN, input_file);
    ss.ip_proto = (uint16_t*)(header); header += 2;
    ss.is_ipv6 = (uint8_t*)(header); header += 1;
    ss.sport = (uint16_t*)(header); header += sizeof(uint16_t);
    ss.cport = (uint16_t*)(header); header += sizeof(uint16_t);
    if (ss.is_ipv6) {
        ss.sip.h = (uint64_t*)(header); header += 8;
        ss.sip.l = (uint64_t*)(header); header += 8;
        ss.cip.h = (uint64_t*)(header); header += 8;
        ss.cip.l = (uint64_t*)(header); header += 8;
    }
    else {
        ss.sip = (uint32_t*)(header); header += 16;
        ss.cip = (uint32_t*)(header); header += 16;
    }
    return 0;
}

static int InputDologID(FILE* input_file)
{
    uint32_t count = 0;
    fread(&count, sizeof(uint32_t), 1, input_file);
    uint32_t dologid[DOLOGID_COUNT_MAX]; 
    fread(dologid, sizeof(uint32_t), count, input_file);
}

static int InputStreamPayload();

int PlayBack(FILE* input_file)
{
    Stream ss;
    while (true) {
        memset(&ss, 0, sizeof(ss)); 
        // header
        InputStreamHeader(&ss, input_file);
        // dolog
        InputDologID(input_file);
        while (true) {
            // stream
            PushStream() 
        }
    }

    return 0;
}

int main(int argc, char** argv)
{
    int err_code;
    if ((err_code = CreateEngine()) != ERROR_NORMAL) {
        printf("%s\n", GetErrorMsg(err_code));
        return -1;
    }

    FILE* input_file = fopen("1234.bak", "rb");
    PlayBack (input_file);

    DestroyEngine();

    return 0;
}
