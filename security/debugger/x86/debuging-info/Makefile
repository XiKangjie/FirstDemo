CC=gcc
CFLAGS=-g

all: tracedprog2 dwarf_get_func_addr

tracedprog2: tracedprog2.c
	$(CC) $(CFLAGS) -o tracedprog2 tracedprog2.c

# sudo yum install libdwarf-devel (epel for centos)
dwarf_get_func_addr: dwarf_get_func_addr.c
	$(CC) $(CFLAGS) -o dwarf_get_func_addr dwarf_get_func_addr.c -ldwarf

clean:
	rm tracedprog2 dwarf_get_func_addr
