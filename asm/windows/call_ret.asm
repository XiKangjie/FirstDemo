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
    ;var1 db 0
.code

start:
    ;; 1. save caller-saved registers EAX, ECX, EDX

    ;; 2. push paramters onto the stack
    push 1          ; Push last parameter first
    push 1          ; Push the second parameter
    xor eax, eax
    push eax        ; Push first parameter last 

    ;; 3. call the subroutine
    call main       ; This instruction places the return address on top of the parameters
                    ; on the stack, and branches to the subroutine code.
    ; After the subroutine returns(immediately following the 'call' instruction),
    ; the return value is in the register EAX.
    ;print str$(eax)
    ;print chr$(13, 10)

    ; Restore the machine state
    ;; 4. (<--2) Remove the parameters from stack
    add esp, 12

    ;; 5. (<--1) Restore the contents of caller-saved registers(EAX, ECX, EDX)
   
    exit

main proc
    ;print chr$("Function Call.", 13, 10)

    ; Subroutine Prologue
    ;; 1. Push the value of EBP onto the stack, and then copy the value of ESP into EBP
    push ebp        ; Save the old base pointer value. (maintains the base pointer, EBP)
    mov ebp, esp    ; Set the new base pointer value. (for accessing parameters and local variables)

    ;; 2. Allocate local variables by making space on the stack
    sub esp, 4      ; Make room for one 4-byte local variable.

    ;; 3. Save the values of the callee-saved registers that will be used by the function must be saved.
    ; (EBX, EDI, ESI)
    push edi        ; Save the values of registers that the function
    push esi        ; will modify. This function uses EDI and ESI.
                    ; (no need to save EBX, EBP, or ESP)

    ; Subroutine Body
    mov eax, [ebp + 8]      ; Move value of parameter 1 into EAX
    mov esi, [ebp + 12]     ; Move value of parameter 2 into ESI
    mov edi, [ebp + 16]     ; Move value of parameter 3 into EDI

    mov [ebp - 4], edi      ; Move EDI into the local variable
    add [ebp - 4], esi      ; Add ESI into the local variable

    ;; 4. Leave the return value in EAX
    add eax, [ebp - 4]      ; Add the contents of the local variables
                            ; into EAX (final result)

    ; Subroutine Epilogue
    ;; 5. (<--3) Restore the old values of any callee-saved registers(EDI and ESI) that were modified.
    pop esi                 ; in the inverse order
    pop edi

    ;; 6. (<--2) Deallocate local variables.
    mov esp, ebp            ; This works because the base pointer always contains the value that
                            ; the stack pointer contained immediately prior to the allocation of the local variables

    ;; 7. (<--1) Restore the caller's base pointer value
    pop ebp

    ;; 8. Return to the caller by executing a ret instruction.
    ret                     ; pops return address, and jump to return address.

main endp

end start