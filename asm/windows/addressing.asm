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

.data
    num dd 10
    lpnum dd ?
    hex dd 12345678h
    array dd 10 dup(2)
    array2 dd 1, 2, 3, 4

    itm0 dd 0
    itm1 dd 1
    array3 dd itm0, itm1

.code
start:
    call main
    inkey
    exit

main proc
    push esi

    mov eax, num
    print str$(eax)         ; 10 (value not address)
    print chr$(13, 10)

    mov eax, array          ; 2 (value not address)
    print str$(eax)
    print chr$(13, 10)

    mov esi, array          ; 2 (value not address, have nothing to do with register type)
    print str$(esi)
    print chr$(13, 10)

    mov eax, array2         ; 1 (also value)
    print str$(eax)
    print chr$(13, 10)

    mov eax, array2 + 4     ; 2 (access to second value of array)
    print str$(eax)
    print chr$(13, 10)

    lea eax, itm0
    print str$(eax)         ; 4206660
    print chr$(13, 10)

    mov eax, array3         ; 4206660 (address of itm0)
    print str$(eax)
    print chr$(13, 10)


    lea eax, num
    mov lpnum, eax
    print str$(eax)         ; 4206592 (lpnum value is address of num)
    print chr$(13, 10)


    lea eax, lpnum
    print str$(eax)         ; 4206596 (eax value is address of lpnum)
    print chr$(13, 10)

    mov eax, lpnum
    mov eax, [eax]          ; [] used for registers. A register enclosed in square brackets is effectively a memory operand.
    print str$(eax)         ; 10 (doule pointer)
    print chr$(13, 10)

    mov eax, [lpnum]        ; 4206592 (still the address of the num, not the value of num)
    print str$(eax)
    print chr$(13, 10)

    lea eax, hex
    print str$(eax)
    print chr$(13, 10)

    pop esi
    
    ret
main endp

end start