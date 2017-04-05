#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * https://blog.holbertonschool.com/hack-the-virtual-memory-drawing-the-vm-diagram/
 *
 * main - print locations of various elements
 *
 * Return: EXIT_FAILURE if something failed. Otherwise EXIT_SUCCESS
 */
int main(int ac, char **av, char **env)
{
    int a;
    void *p;
    int i;
    
    // stack
    printf("Address of a: %p\n", &a);
    printf("\n");

    // heap
    p = malloc(98);
    if (p == NULL)
    {
            fprintf(stderr, "Can't malloc\n");
            return (EXIT_FAILURE);
    }
    printf("Allocated space in the heap: %p\n", p);
    printf("\n");

    // code
    printf("Address of function main: %p\n", main);
    printf("First bytes of the main function:\n\t");
    for (i = 0; i < 15; i++)
    {
            printf("%02x ", ((unsigned char *)main)[i]);
    }
    printf("\n\n");

    // argc argv
    printf("Address of the count of arguments: %p\n", &ac);
    printf("Address of the array of arguments: %p\n", av);
    printf("Addresses of the arguments:\n\t");
    for (i = 0; i < ac; i++)
    {
            printf("[%s]:%p ", av[i], av[i]);
    }
    printf("\n\n");

    // env
    printf("Address of the array of environment variables: %p\n", env);
    printf("Address of the first environment variable: \n");
    for(i = 0; i < 3; i++)
    {
        printf("\t[%p]:\"%s\"\n", env[i], env[i]);
    }
    getchar();
    return (EXIT_SUCCESS);
}
