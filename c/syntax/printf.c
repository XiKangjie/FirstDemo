#include <stdio.h>

int main()
{
    char* str = "hello world!";
    printf("%s\n", str);
    /*
       An optional precision, in the form of a period ('.')  followed by an
       optional decimal digit string.  Instead of a decimal digit string one
       may write "*" or "*m$" (for some decimal integer m) to specify that
       the precision is given in the next argument, or in the m-th argument,
       respectively, which must be of type int.
    */
    printf("%.*s\n", 5, str);

    return 0;
}


/*

hello world!
hello

*/
