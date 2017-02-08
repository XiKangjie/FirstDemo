; nasm hello.asm
; ndisasm -b64 hello
bits 64

jmp short one

two:
    pop rsi
    xor rax, rax
    ;inc rax
    mov al, 1
    ;xor rdi, rdi
    ;inc rdi
    mov rdi, rax
    xor rdx, rdx
    mov dl, 14 
    syscall
    mov al, 60
    xor rdi, rdi
    syscall

one:
    call two
    db "hello, world!", 0xa
