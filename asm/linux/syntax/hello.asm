; nasm -f elf64 -o hello.o hello.asm
; ld -o hello.exe hello.o

section .data
    msg db  "hello, world!"

section .text
    global _start

_start:
    mov rax, 1      ; write syscall
    mov rdi, 1      ; 1st arg, file descriptor, standard output
    mov rsi, msg    ; 2nd arg, message address
    mov rdx, 13     ; 3rd arg, length of message
    syscall
    mov rax, 60     ; exit syscall
    mov rdi, 0      ; exit code
    syscall
