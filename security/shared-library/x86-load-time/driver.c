/*
 * $ gcc -g -c driver.c -o driver.o
 * $ gcc -o driver driver.o -L. -lmlreloc
 *
 * $ sudo ldconfig $(pwd)
 */

#define _GNU_SOURCE
#include <link.h>
#include <stdlib.h>
#include <stdio.h>

extern int ml_func(int, int);

static int header_handler(struct dl_phdr_info* info, size_t size, void* data)
{
    printf("name=%s (%d segments) address=%p\n",
            info->dlpi_name, info->dlpi_phnum, (void*)info->dlpi_addr);
    int j;
    for (j = 0; j < info->dlpi_phnum; j++) {
         printf("\t\t header %2d: address=%10p\n", j,
             (void*) (info->dlpi_addr + info->dlpi_phdr[j].p_vaddr));
         printf("\t\t\t type=%u, flags=0x%X\n",
                 info->dlpi_phdr[j].p_type, info->dlpi_phdr[j].p_flags);
    }
    printf("\n");
    return 0;
}

int main(int argc, const char* argv[])
{
    dl_iterate_phdr(header_handler, NULL);

    int t = ml_func(argc, argc);
    return t;
}
