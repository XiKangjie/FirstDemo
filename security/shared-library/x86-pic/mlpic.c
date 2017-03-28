/*
 * http://eli.thegreenplace.net/2011/11/03/position-independent-code-pic-in-shared-libraries/
 *
 * gcc -g -shared -fpic -o libmlpic.so mlpic.c
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
