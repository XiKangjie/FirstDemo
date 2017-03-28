/*
 * http://eli.thegreenplace.net/2011/08/25/load-time-relocation-of-shared-libraries/
 *
 * gcc -g -c ml2_main.c -o ml2_mainreloc.o
 * gcc -shared -o libml2reloc.so ml2_mainreloc.o
 */
int myglob = 42;

int ml_util_func(int a)
{
    return a + 1;
}

int ml_func(int a, int b)
{
    int c = b + ml_util_func(a);
    myglob += c;
    return b + myglob;
}
