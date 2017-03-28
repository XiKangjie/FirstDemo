/*
 * gcc -g -o driver -shared -fpic driver.c -L ./ -l mlpic
 */

extern int ml_func(int a, int b);

int main() 
{
    ml_func(1, 2);

    return 0;
}
