.386
.model flat, stdcall

option casemap :none

include \masm32\include\windows.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc

includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

WinMain proto :DWORD, :DWORD, :DWORD, :DWORD
WndProc proto :HWND, :UINT, :WPARAM, :LPARAM

.const
        EditID      equ 100
        ButtonID    equ 101
.data
        ClassName       db  "WinClass", 0
        AppName         db  "Simple Window", 0
        EditClassName   db  "edit", 0
        ButtonClassName db  "button", 0
        ButtonText      db  "click me", 0
        ButtonSpeak     db  "I'm a button!", 0

.data?
        hInstance   HINSTANCE   ?
        hEdit       HWND        ?
        hButton     HWND        ?

.code
start:
        invoke GetModuleHandle, NULL
        mov hInstance, eax
        invoke WinMain, hInstance, NULL, NULL, 0
        invoke ExitProcess, eax

WinMain proc hInst:HINSTANCE, hPrevInst:HINSTANCE, CmdLine:LPSTR, CmdShow:DWORD
        local wc:WNDCLASSEX
        local msg:MSG
        local hwnd:HWND

        mov     wc.cbSize, SIZEOF WNDCLASSEX
        mov     wc.style, CS_HREDRAW or CS_VREDRAW
        mov     wc.lpfnWndProc, offset WndProc
        mov     wc.cbClsExtra, NULL
        mov     wc.cbWndExtra, NULL
        push    hInstance
        pop     wc.hInstance
        mov     wc.hbrBackground, COLOR_WINDOW + 1
        mov     wc.lpszMenuName, NULL
        mov     wc.lpszClassName, offset ClassName
        invoke  LoadIcon, NULL, IDI_APPLICATION
        mov     wc.hIcon, eax
        mov     wc.hIconSm, eax
        invoke  LoadCursor, NULL, IDC_ARROW
        mov     wc.hCursor, eax
        
        invoke  RegisterClassEx, addr wc

        invoke CreateWindowEx, 0, 
                               addr ClassName,
                               addr AppName, 
                               WS_OVERLAPPEDWINDOW or WS_VISIBLE, 
                               CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,CW_USEDEFAULT, 
                               NULL, NULL, 
                               hInst, NULL
        mov     hwnd, eax

        .while TRUE
                invoke GetMessage, addr msg, NULL, 0, 0
                .break .if (!eax)
                invoke TranslateMessage, addr msg
                invoke DispatchMessage, addr msg
        .endw

        mov eax, msg.wParam
        ret
WinMain endp

WndProc proc hWnd:HWND, uMsg:UINT, wParam:WPARAM, lParam:LPARAM
        .if uMsg == WM_DESTROY
                invoke PostQuitMessage, 0
        .elseif uMsg == WM_CREATE
                invoke CreateWindowEx, NULL,
                                       addr ButtonClassName,
                                       addr ButtonText,
                                       WS_CHILD or WS_VISIBLE or BS_DEFPUSHBUTTON,
                                       10, 50, 80, 30,
                                       hWnd, ButtonID,
                                       hInstance, NULL
                mov hButton, eax
                invoke CreateWindowEx, WS_EX_CLIENTEDGE,
                                       addr EditClassName,
                                       NULL,
                                       WS_CHILD or WS_VISIBLE,
                                       10, 10, 100, 20,
                                       hWnd, EditID,
                                       hInstance, NULL
                mov hEdit, eax
        .elseif uMsg == WM_COMMAND
                mov eax, wParam
                .if ax == ButtonID
                        shr eax, 16
                        .if ax == BN_CLICKED
                                invoke MessageBox, NULL, addr ButtonSpeak, addr ButtonSpeak, MB_OK
                        .endif
                .endif                        
        .else
                invoke DefWindowProc, hWnd, uMsg, wParam, lParam
                ret
        .endif
        xor eax, eax
        ret
WndProc endp 

end start     