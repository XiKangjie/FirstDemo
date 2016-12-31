obj-m += hello.o

all:
	make -C /lib/modules/2.6.32-220.el6.x86_64/build M=$(PWD) modules

clean:
	make -C /lib/modules/2.6.32-220.el6.x86_64/build M=$(PWD) clean
