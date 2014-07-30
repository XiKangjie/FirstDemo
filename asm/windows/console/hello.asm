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

    .code

start:
    print chr$("Hey, this actually works.", 13, 10)
    exit

end start