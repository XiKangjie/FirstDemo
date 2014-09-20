; nasm -f elf64 -o sum.o sum.asm
; ld -o sum.exe sum.o

; initialised data section
section .data
    ; define constants
    num1:   equ 100
    num2:   equ 50
    ; initialize message
    msg:    db  "Sum is correct.\n"

section .text
    global _start
; entry point
_start:
    mov rax, num1
    mov rbx, num2
    add rax, rbx
    cmp rax, 150
    jne .exit
    jmp .rightSum

; print message that sum is correct
.rightSum:
    ; write systall
    mov rax, 1
    ; file descriptor, standard output
    mov rdi, 1
    ; message address
    mov rsi, msg
    ; lenghth of message
    mov rdx, 16
    ; call write syscall
    syscall
    ; exit from program
    jmp .exit

; exit procedure
.exit:
    ; exit syscall
    mov rax, 60
    ; exit code
    mov rdi, 0
    syscall
