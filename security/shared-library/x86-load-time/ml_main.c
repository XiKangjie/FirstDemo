/*
 * http://eli.thegreenplace.net/2011/08/25/load-time-relocation-of-shared-libraries/
 *
 * gcc -g -c ml_main.c -o ml_mainreloc.o
 * gcc -shared -o libmlreloc.so ml_mainreloc.o
 */

int myglob = 42;

int ml_func(int a, int b)
{
    myglob += a;
    return b + myglob;
}
