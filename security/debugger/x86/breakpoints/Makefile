CC=gcc
CFLAGS=-g -std=c99

all: traced_printer2 bp_manual traced_c_loop bp_use_lib

traced_printer2: traced_printer2.asm
	nasm -f elf32 -o traced_printer2.o traced_printer2.asm
	ld -o traced_printer2 traced_printer2.o

bp_manual: bp_manual.c debuglib.c debuglib.h
	$(CC) $(CFLAGS) -o bp_manual bp_manual.c debuglib.c

traced_c_loop:
	$(CC) $(CFLAGS) -o traced_c_loop traced_c_loop.c

bp_use_lib: bp_use_lib.c debuglib.c debuglib.h
	$(CC) $(CFLAGS) -o bp_use_lib bp_use_lib.c debuglib.c

clean:
	rm traced_printer2 bp_manual traced_c_loop bp_use_lib *.o
