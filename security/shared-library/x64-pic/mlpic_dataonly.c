/*
 * http://eli.thegreenplace.net/2011/11/11/position-independent-code-pic-in-shared-libraries-on-x64
 *
 * gcc -shared -fpic -o libmlpic_dataonly.so mlpic_dataonly.c
 */

int myglob = 42;

int ml_func(int a, int b)
{
    return myglob + a + b;
}
