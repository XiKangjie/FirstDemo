.386
.model flat, stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\macros\macros.asm

include \masm32\include\masm32.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc

includelib \masm32\lib\masm32.lib
includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

.data
    itm0 dd 0
    itm1 dd 1
    itm2 dd 2
    itm3 dd 3
    itm4 dd 4
    itm5 dd 5
    itm6 dd 6
    itm7 dd 7
    itm8 dd 8
    itm9 dd 9

    array dd itm0, itm1, itm2, itm3, itm4
          dd itm5, itm6, itm7, itm8, itm9

.code
start:
    call main
    exit

main proc
    local cnt:dword

    push ebx
    push esi
    push edi

    mov cnt, 10

    mov ebx, array
    xor esi, esi

    print chr$("Index being changed", 13, 10)

label2:
    mov edi, [ebx + esi * 4]
    print str$(edi)
    print chr$(13, 10)
    add esi, 1
    sub cnt, 1
    jnz label2

    print chr$("Displacement being changed", 13, 10)

    xor esi, esi

    mov edi, [ebx + esi * 4]
    print str$(edi)
    print chr$(13, 10)

    mov edi, [ebx + esi * 4 + 4]
    print str$(edi)
    print chr$(13, 10)

    mov edi, [ebx + esi * 4 + 8]
    print str$(edi)
    print chr$(13, 10)

    mov edi, [ebx + esi * 4 + 12]
    print str$(edi)
    print chr$(13, 10)

    pop edi
    pop esi
    pop ebx

    ret

main endp

end start