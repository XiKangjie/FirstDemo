obj-m += sys_call_table.o

KERNEL_TREE := /home/xikangjie/download/linux-4.14-debug/linux-4.14

all:
	make -C $(KERNEL_TREE) M=$(PWD) modules

clean:
	make -C $(KERNEL_TREE) M=$(PWD) clean
