bits 64

push byte 1
pop rax
mov rdi, rax
; http://stackoverflow.com/questions/13351363/push-on-64bit-intel-osx
;push 0x68732f2f6e69622f; /bin//sh ; echo -n /bin//sh | hexdump -C
mov rcx, 0x68732f2f6e69622f
push rcx
mov rsi, rsp
push byte 8
pop rdx
syscall
mov al, 60 
xor rdi, rdi
syscall
