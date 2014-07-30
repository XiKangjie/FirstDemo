.386
.model flat, stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\macros\macros.asm

include \masm32\include\masm32.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc
include \masm32\include\msvcrt.inc

includelib \masm32\lib\masm32.lib
includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\msvcrt.lib

.code

start:
    call main
    exit

main proc
    local var1:dword
    local str1:dword

    mov eax, 100
    mov ecx, 250
    add ecx, eax
    print str$(ecx)
    print chr$(13, 10, 13, 10)

    ;mov var1, sval(input("Enter a number : "))
    mov str1, input("Enter a number : ")
    mov var1, sval(str1)
    cmp var1, 100
    je equal
    jg bigger
    jl smaller

equal:
    print chr$("The number you entered is 100", 13, 10)
    jmp over

bigger:
    print chr$("The number you entered is greater than 100", 13, 10)
    jmp over

smaller:
    print chr$("The number you entered is smaller than 100", 13, 10)

over:
    ret

main endp

end start