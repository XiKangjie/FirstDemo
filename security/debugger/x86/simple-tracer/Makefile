CC=gcc
CFLAGS=-g

all: traced_helloworld simple_tracer

traced_helloworld: traced_helloworld.asm
	nasm -f elf32 -o traced_helloworld.o traced_helloworld.asm
	ld -o traced_helloworld traced_helloworld.o

simple_tracer: simple_tracer.c
	$(CC) $(CFLAGS) -o simple_tracer simple_tracer.c

clean:
	rm traced_helloworld simple_tracer *.o
