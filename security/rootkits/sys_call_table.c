/*  
 *  hello-2.c - Demonstrating the module_init() and module_exit() macros.
 *  This is preferred over using init_module() and cleanup_module().
 */
#include <linux/module.h>   /* Needed by all modules */
#include <linux/kernel.h>   /* Needed for KERN_INFO */
#include <linux/init.h>     /* Needed for the macros */
#include <linux/syscalls.h>

#define START_CHECK 0xffffffff81000000
#define END_CHECK 0xffffffffa2000000
typedef unsigned long psize;

psize **find(void) {
    psize **sctable;
    psize i = START_CHECK;
    while (i < END_CHECK) {
        sctable = (psize **) i;
        if (sctable[__NR_close] == (psize *) sys_close) {
            return &sctable[0];
        }
        i += sizeof(void *);
    }
    return NULL;
}

static int __init find_init(void)
{
    printk(KERN_INFO "sys_call_table: %p\n", find());
    return 0;
}

static void __exit find_exit(void)
{
    printk(KERN_INFO "Goodbye\n");
}

module_init(find_init);
module_exit(find_exit);
