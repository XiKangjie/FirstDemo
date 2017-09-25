
/opt/fusion/bin/level00:     file format elf32-i386


Disassembly of section .init:

0804888c <_init>:
 804888c:	53                   	push   ebx
 804888d:	83 ec 08             	sub    esp,0x8
 8048890:	e8 00 00 00 00       	call   8048895 <_init+0x9>
 8048895:	5b                   	pop    ebx
 8048896:	81 c3 57 2b 00 00    	add    ebx,0x2b57
 804889c:	8b 83 fc ff ff ff    	mov    eax,DWORD PTR [ebx-0x4]
 80488a2:	85 c0                	test   eax,eax
 80488a4:	74 05                	je     80488ab <_init+0x1f>
 80488a6:	e8 55 01 00 00       	call   8048a00 <__gmon_start__@plt>
 80488ab:	e8 50 03 00 00       	call   8048c00 <frame_dummy>
 80488b0:	e8 ab 11 00 00       	call   8049a60 <__do_global_ctors_aux>
 80488b5:	83 c4 08             	add    esp,0x8
 80488b8:	5b                   	pop    ebx
 80488b9:	c3                   	ret    

Disassembly of section .plt:

080488c0 <setsockopt@plt-0x10>:
 80488c0:	ff 35 f0 b3 04 08    	push   DWORD PTR ds:0x804b3f0
 80488c6:	ff 25 f4 b3 04 08    	jmp    DWORD PTR ds:0x804b3f4
 80488cc:	00 00                	add    BYTE PTR [eax],al
	...

080488d0 <setsockopt@plt>:
 80488d0:	ff 25 f8 b3 04 08    	jmp    DWORD PTR ds:0x804b3f8
 80488d6:	68 00 00 00 00       	push   0x0
 80488db:	e9 e0 ff ff ff       	jmp    80488c0 <_init+0x34>

080488e0 <dup2@plt>:
 80488e0:	ff 25 fc b3 04 08    	jmp    DWORD PTR ds:0x804b3fc
 80488e6:	68 08 00 00 00       	push   0x8
 80488eb:	e9 d0 ff ff ff       	jmp    80488c0 <_init+0x34>

080488f0 <setresuid@plt>:
 80488f0:	ff 25 00 b4 04 08    	jmp    DWORD PTR ds:0x804b400
 80488f6:	68 10 00 00 00       	push   0x10
 80488fb:	e9 c0 ff ff ff       	jmp    80488c0 <_init+0x34>

08048900 <read@plt>:
 8048900:	ff 25 04 b4 04 08    	jmp    DWORD PTR ds:0x804b404
 8048906:	68 18 00 00 00       	push   0x18
 804890b:	e9 b0 ff ff ff       	jmp    80488c0 <_init+0x34>

08048910 <printf@plt>:
 8048910:	ff 25 08 b4 04 08    	jmp    DWORD PTR ds:0x804b408
 8048916:	68 20 00 00 00       	push   0x20
 804891b:	e9 a0 ff ff ff       	jmp    80488c0 <_init+0x34>

08048920 <signal@plt>:
 8048920:	ff 25 0c b4 04 08    	jmp    DWORD PTR ds:0x804b40c
 8048926:	68 28 00 00 00       	push   0x28
 804892b:	e9 90 ff ff ff       	jmp    80488c0 <_init+0x34>

08048930 <memcmp@plt>:
 8048930:	ff 25 10 b4 04 08    	jmp    DWORD PTR ds:0x804b410
 8048936:	68 30 00 00 00       	push   0x30
 804893b:	e9 80 ff ff ff       	jmp    80488c0 <_init+0x34>

08048940 <wait@plt>:
 8048940:	ff 25 14 b4 04 08    	jmp    DWORD PTR ds:0x804b414
 8048946:	68 38 00 00 00       	push   0x38
 804894b:	e9 70 ff ff ff       	jmp    80488c0 <_init+0x34>

08048950 <htons@plt>:
 8048950:	ff 25 18 b4 04 08    	jmp    DWORD PTR ds:0x804b418
 8048956:	68 40 00 00 00       	push   0x40
 804895b:	e9 60 ff ff ff       	jmp    80488c0 <_init+0x34>

08048960 <err@plt>:
 8048960:	ff 25 1c b4 04 08    	jmp    DWORD PTR ds:0x804b41c
 8048966:	68 48 00 00 00       	push   0x48
 804896b:	e9 50 ff ff ff       	jmp    80488c0 <_init+0x34>

08048970 <setgroups@plt>:
 8048970:	ff 25 20 b4 04 08    	jmp    DWORD PTR ds:0x804b420
 8048976:	68 50 00 00 00       	push   0x50
 804897b:	e9 40 ff ff ff       	jmp    80488c0 <_init+0x34>

08048980 <accept@plt>:
 8048980:	ff 25 24 b4 04 08    	jmp    DWORD PTR ds:0x804b424
 8048986:	68 58 00 00 00       	push   0x58
 804898b:	e9 30 ff ff ff       	jmp    80488c0 <_init+0x34>

08048990 <fwrite@plt>:
 8048990:	ff 25 28 b4 04 08    	jmp    DWORD PTR ds:0x804b428
 8048996:	68 60 00 00 00       	push   0x60
 804899b:	e9 20 ff ff ff       	jmp    80488c0 <_init+0x34>

080489a0 <strcpy@plt>:
 80489a0:	ff 25 2c b4 04 08    	jmp    DWORD PTR ds:0x804b42c
 80489a6:	68 68 00 00 00       	push   0x68
 80489ab:	e9 10 ff ff ff       	jmp    80488c0 <_init+0x34>

080489b0 <getpid@plt>:
 80489b0:	ff 25 30 b4 04 08    	jmp    DWORD PTR ds:0x804b430
 80489b6:	68 70 00 00 00       	push   0x70
 80489bb:	e9 00 ff ff ff       	jmp    80488c0 <_init+0x34>

080489c0 <daemon@plt>:
 80489c0:	ff 25 34 b4 04 08    	jmp    DWORD PTR ds:0x804b434
 80489c6:	68 78 00 00 00       	push   0x78
 80489cb:	e9 f0 fe ff ff       	jmp    80488c0 <_init+0x34>

080489d0 <setrlimit@plt>:
 80489d0:	ff 25 38 b4 04 08    	jmp    DWORD PTR ds:0x804b438
 80489d6:	68 80 00 00 00       	push   0x80
 80489db:	e9 e0 fe ff ff       	jmp    80488c0 <_init+0x34>

080489e0 <malloc@plt>:
 80489e0:	ff 25 3c b4 04 08    	jmp    DWORD PTR ds:0x804b43c
 80489e6:	68 88 00 00 00       	push   0x88
 80489eb:	e9 d0 fe ff ff       	jmp    80488c0 <_init+0x34>

080489f0 <strerror@plt>:
 80489f0:	ff 25 40 b4 04 08    	jmp    DWORD PTR ds:0x804b440
 80489f6:	68 90 00 00 00       	push   0x90
 80489fb:	e9 c0 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a00 <__gmon_start__@plt>:
 8048a00:	ff 25 44 b4 04 08    	jmp    DWORD PTR ds:0x804b444
 8048a06:	68 98 00 00 00       	push   0x98
 8048a0b:	e9 b0 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a10 <exit@plt>:
 8048a10:	ff 25 48 b4 04 08    	jmp    DWORD PTR ds:0x804b448
 8048a16:	68 a0 00 00 00       	push   0xa0
 8048a1b:	e9 a0 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a20 <realpath@plt>:
 8048a20:	ff 25 4c b4 04 08    	jmp    DWORD PTR ds:0x804b44c
 8048a26:	68 a8 00 00 00       	push   0xa8
 8048a2b:	e9 90 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a30 <open@plt>:
 8048a30:	ff 25 50 b4 04 08    	jmp    DWORD PTR ds:0x804b450
 8048a36:	68 b0 00 00 00       	push   0xb0
 8048a3b:	e9 80 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a40 <srand@plt>:
 8048a40:	ff 25 54 b4 04 08    	jmp    DWORD PTR ds:0x804b454
 8048a46:	68 b8 00 00 00       	push   0xb8
 8048a4b:	e9 70 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a50 <strchr@plt>:
 8048a50:	ff 25 58 b4 04 08    	jmp    DWORD PTR ds:0x804b458
 8048a56:	68 c0 00 00 00       	push   0xc0
 8048a5b:	e9 60 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a60 <__libc_start_main@plt>:
 8048a60:	ff 25 5c b4 04 08    	jmp    DWORD PTR ds:0x804b45c
 8048a66:	68 c8 00 00 00       	push   0xc8
 8048a6b:	e9 50 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a70 <fprintf@plt>:
 8048a70:	ff 25 60 b4 04 08    	jmp    DWORD PTR ds:0x804b460
 8048a76:	68 d0 00 00 00       	push   0xd0
 8048a7b:	e9 40 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a80 <execve@plt>:
 8048a80:	ff 25 64 b4 04 08    	jmp    DWORD PTR ds:0x804b464
 8048a86:	68 d8 00 00 00       	push   0xd8
 8048a8b:	e9 30 fe ff ff       	jmp    80488c0 <_init+0x34>

08048a90 <write@plt>:
 8048a90:	ff 25 68 b4 04 08    	jmp    DWORD PTR ds:0x804b468
 8048a96:	68 e0 00 00 00       	push   0xe0
 8048a9b:	e9 20 fe ff ff       	jmp    80488c0 <_init+0x34>

08048aa0 <bind@plt>:
 8048aa0:	ff 25 6c b4 04 08    	jmp    DWORD PTR ds:0x804b46c
 8048aa6:	68 e8 00 00 00       	push   0xe8
 8048aab:	e9 10 fe ff ff       	jmp    80488c0 <_init+0x34>

08048ab0 <setvbuf@plt>:
 8048ab0:	ff 25 70 b4 04 08    	jmp    DWORD PTR ds:0x804b470
 8048ab6:	68 f0 00 00 00       	push   0xf0
 8048abb:	e9 00 fe ff ff       	jmp    80488c0 <_init+0x34>

08048ac0 <snprintf@plt>:
 8048ac0:	ff 25 74 b4 04 08    	jmp    DWORD PTR ds:0x804b474
 8048ac6:	68 f8 00 00 00       	push   0xf8
 8048acb:	e9 f0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048ad0 <__errno_location@plt>:
 8048ad0:	ff 25 78 b4 04 08    	jmp    DWORD PTR ds:0x804b478
 8048ad6:	68 00 01 00 00       	push   0x100
 8048adb:	e9 e0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048ae0 <asprintf@plt>:
 8048ae0:	ff 25 7c b4 04 08    	jmp    DWORD PTR ds:0x804b47c
 8048ae6:	68 08 01 00 00       	push   0x108
 8048aeb:	e9 d0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048af0 <rand@plt>:
 8048af0:	ff 25 80 b4 04 08    	jmp    DWORD PTR ds:0x804b480
 8048af6:	68 10 01 00 00       	push   0x110
 8048afb:	e9 c0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b00 <fork@plt>:
 8048b00:	ff 25 84 b4 04 08    	jmp    DWORD PTR ds:0x804b484
 8048b06:	68 18 01 00 00       	push   0x118
 8048b0b:	e9 b0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b10 <errx@plt>:
 8048b10:	ff 25 88 b4 04 08    	jmp    DWORD PTR ds:0x804b488
 8048b16:	68 20 01 00 00       	push   0x120
 8048b1b:	e9 a0 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b20 <htonl@plt>:
 8048b20:	ff 25 8c b4 04 08    	jmp    DWORD PTR ds:0x804b48c
 8048b26:	68 28 01 00 00       	push   0x128
 8048b2b:	e9 90 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b30 <listen@plt>:
 8048b30:	ff 25 90 b4 04 08    	jmp    DWORD PTR ds:0x804b490
 8048b36:	68 30 01 00 00       	push   0x130
 8048b3b:	e9 80 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b40 <socket@plt>:
 8048b40:	ff 25 94 b4 04 08    	jmp    DWORD PTR ds:0x804b494
 8048b46:	68 38 01 00 00       	push   0x138
 8048b4b:	e9 70 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b50 <setresgid@plt>:
 8048b50:	ff 25 98 b4 04 08    	jmp    DWORD PTR ds:0x804b498
 8048b56:	68 40 01 00 00       	push   0x140
 8048b5b:	e9 60 fd ff ff       	jmp    80488c0 <_init+0x34>

08048b60 <close@plt>:
 8048b60:	ff 25 9c b4 04 08    	jmp    DWORD PTR ds:0x804b49c
 8048b66:	68 48 01 00 00       	push   0x148
 8048b6b:	e9 50 fd ff ff       	jmp    80488c0 <_init+0x34>

Disassembly of section .text:

08048b70 <_start>:
 8048b70:	31 ed                	xor    ebp,ebp
 8048b72:	5e                   	pop    esi
 8048b73:	89 e1                	mov    ecx,esp
 8048b75:	83 e4 f0             	and    esp,0xfffffff0
 8048b78:	50                   	push   eax
 8048b79:	54                   	push   esp
 8048b7a:	52                   	push   edx
 8048b7b:	68 50 9a 04 08       	push   0x8049a50
 8048b80:	68 e0 99 04 08       	push   0x80499e0
 8048b85:	51                   	push   ecx
 8048b86:	56                   	push   esi
 8048b87:	68 91 99 04 08       	push   0x8049991
 8048b8c:	e8 cf fe ff ff       	call   8048a60 <__libc_start_main@plt>
 8048b91:	f4                   	hlt    
 8048b92:	90                   	nop
 8048b93:	90                   	nop
 8048b94:	90                   	nop
 8048b95:	90                   	nop
 8048b96:	90                   	nop
 8048b97:	90                   	nop
 8048b98:	90                   	nop
 8048b99:	90                   	nop
 8048b9a:	90                   	nop
 8048b9b:	90                   	nop
 8048b9c:	90                   	nop
 8048b9d:	90                   	nop
 8048b9e:	90                   	nop
 8048b9f:	90                   	nop

08048ba0 <__do_global_dtors_aux>:
 8048ba0:	55                   	push   ebp
 8048ba1:	89 e5                	mov    ebp,esp
 8048ba3:	53                   	push   ebx
 8048ba4:	83 ec 04             	sub    esp,0x4
 8048ba7:	80 3d e4 b4 04 08 00 	cmp    BYTE PTR ds:0x804b4e4,0x0
 8048bae:	75 3f                	jne    8048bef <__do_global_dtors_aux+0x4f>
 8048bb0:	a1 e8 b4 04 08       	mov    eax,ds:0x804b4e8
 8048bb5:	bb 08 b3 04 08       	mov    ebx,0x804b308
 8048bba:	81 eb 04 b3 04 08    	sub    ebx,0x804b304
 8048bc0:	c1 fb 02             	sar    ebx,0x2
 8048bc3:	83 eb 01             	sub    ebx,0x1
 8048bc6:	39 d8                	cmp    eax,ebx
 8048bc8:	73 1e                	jae    8048be8 <__do_global_dtors_aux+0x48>
 8048bca:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
 8048bd0:	83 c0 01             	add    eax,0x1
 8048bd3:	a3 e8 b4 04 08       	mov    ds:0x804b4e8,eax
 8048bd8:	ff 14 85 04 b3 04 08 	call   DWORD PTR [eax*4+0x804b304]
 8048bdf:	a1 e8 b4 04 08       	mov    eax,ds:0x804b4e8
 8048be4:	39 d8                	cmp    eax,ebx
 8048be6:	72 e8                	jb     8048bd0 <__do_global_dtors_aux+0x30>
 8048be8:	c6 05 e4 b4 04 08 01 	mov    BYTE PTR ds:0x804b4e4,0x1
 8048bef:	83 c4 04             	add    esp,0x4
 8048bf2:	5b                   	pop    ebx
 8048bf3:	5d                   	pop    ebp
 8048bf4:	c3                   	ret    
 8048bf5:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
 8048bf9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

08048c00 <frame_dummy>:
 8048c00:	55                   	push   ebp
 8048c01:	89 e5                	mov    ebp,esp
 8048c03:	83 ec 18             	sub    esp,0x18
 8048c06:	a1 0c b3 04 08       	mov    eax,ds:0x804b30c
 8048c0b:	85 c0                	test   eax,eax
 8048c0d:	74 12                	je     8048c21 <frame_dummy+0x21>
 8048c0f:	b8 00 00 00 00       	mov    eax,0x0
 8048c14:	85 c0                	test   eax,eax
 8048c16:	74 09                	je     8048c21 <frame_dummy+0x21>
 8048c18:	c7 04 24 0c b3 04 08 	mov    DWORD PTR [esp],0x804b30c
 8048c1f:	ff d0                	call   eax
 8048c21:	c9                   	leave  
 8048c22:	c3                   	ret    
 8048c23:	90                   	nop

08048c24 <enable_cores>:
 8048c24:	55                   	push   ebp
 8048c25:	89 e5                	mov    ebp,esp
 8048c27:	83 ec 28             	sub    esp,0x28
 8048c2a:	c7 45 f4 ff ff ff ff 	mov    DWORD PTR [ebp-0xc],0xffffffff
 8048c31:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048c34:	89 45 f0             	mov    DWORD PTR [ebp-0x10],eax
 8048c37:	8d 45 f0             	lea    eax,[ebp-0x10]
 8048c3a:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048c3e:	c7 04 24 04 00 00 00 	mov    DWORD PTR [esp],0x4
 8048c45:	e8 86 fd ff ff       	call   80489d0 <setrlimit@plt>
 8048c4a:	83 f8 ff             	cmp    eax,0xffffffff
 8048c4d:	75 14                	jne    8048c63 <enable_cores+0x3f>
 8048c4f:	c7 44 24 04 b0 9a 04 	mov    DWORD PTR [esp+0x4],0x8049ab0
 8048c56:	08 
 8048c57:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8048c5e:	e8 fd fc ff ff       	call   8048960 <err@plt>
 8048c63:	c9                   	leave  
 8048c64:	c3                   	ret    

08048c65 <child_reaper>:
 8048c65:	55                   	push   ebp
 8048c66:	89 e5                	mov    ebp,esp
 8048c68:	83 ec 28             	sub    esp,0x28
 8048c6b:	8d 45 f4             	lea    eax,[ebp-0xc]
 8048c6e:	89 04 24             	mov    DWORD PTR [esp],eax
 8048c71:	e8 ca fc ff ff       	call   8048940 <wait@plt>
 8048c76:	c9                   	leave  
 8048c77:	c3                   	ret    

08048c78 <handle_signals>:
 8048c78:	55                   	push   ebp
 8048c79:	89 e5                	mov    ebp,esp
 8048c7b:	83 ec 18             	sub    esp,0x18
 8048c7e:	b8 65 8c 04 08       	mov    eax,0x8048c65
 8048c83:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048c87:	c7 04 24 11 00 00 00 	mov    DWORD PTR [esp],0x11
 8048c8e:	e8 8d fc ff ff       	call   8048920 <signal@plt>
 8048c93:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 8048c9a:	00 
 8048c9b:	c7 04 24 0d 00 00 00 	mov    DWORD PTR [esp],0xd
 8048ca2:	e8 79 fc ff ff       	call   8048920 <signal@plt>
 8048ca7:	c9                   	leave  
 8048ca8:	c3                   	ret    

08048ca9 <validate_name>:
 8048ca9:	55                   	push   ebp
 8048caa:	89 e5                	mov    ebp,esp
 8048cac:	83 ec 28             	sub    esp,0x28
 8048caf:	c7 45 f4 00 00 00 00 	mov    DWORD PTR [ebp-0xc],0x0
 8048cb6:	e9 86 00 00 00       	jmp    8048d41 <validate_name+0x98>
 8048cbb:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048cbe:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048cc1:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048cc4:	3c 60                	cmp    al,0x60
 8048cc6:	7e 0d                	jle    8048cd5 <validate_name+0x2c>
 8048cc8:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048ccb:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048cce:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048cd1:	3c 7a                	cmp    al,0x7a
 8048cd3:	7e 68                	jle    8048d3d <validate_name+0x94>
 8048cd5:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048cd8:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048cdb:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048cde:	3c 40                	cmp    al,0x40
 8048ce0:	7e 0d                	jle    8048cef <validate_name+0x46>
 8048ce2:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048ce5:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048ce8:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048ceb:	3c 5a                	cmp    al,0x5a
 8048ced:	7e 4e                	jle    8048d3d <validate_name+0x94>
 8048cef:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048cf2:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048cf5:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048cf8:	3c 2f                	cmp    al,0x2f
 8048cfa:	7e 0d                	jle    8048d09 <validate_name+0x60>
 8048cfc:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048cff:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048d02:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048d05:	3c 39                	cmp    al,0x39
 8048d07:	7e 34                	jle    8048d3d <validate_name+0x94>
 8048d09:	a1 c4 b4 04 08       	mov    eax,ds:0x804b4c4
 8048d0e:	89 c2                	mov    edx,eax
 8048d10:	b8 c4 9a 04 08       	mov    eax,0x8049ac4
 8048d15:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
 8048d19:	c7 44 24 08 23 00 00 	mov    DWORD PTR [esp+0x8],0x23
 8048d20:	00 
 8048d21:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 8048d28:	00 
 8048d29:	89 04 24             	mov    DWORD PTR [esp],eax
 8048d2c:	e8 5f fc ff ff       	call   8048990 <fwrite@plt>
 8048d31:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8048d38:	e8 d3 fc ff ff       	call   8048a10 <exit@plt>
 8048d3d:	83 45 f4 01          	add    DWORD PTR [ebp-0xc],0x1
 8048d41:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048d44:	03 45 08             	add    eax,DWORD PTR [ebp+0x8]
 8048d47:	0f b6 00             	movzx  eax,BYTE PTR [eax]
 8048d4a:	84 c0                	test   al,al
 8048d4c:	0f 85 69 ff ff ff    	jne    8048cbb <validate_name+0x12>
 8048d52:	c9                   	leave  
 8048d53:	c3                   	ret    

08048d54 <background_process>:
 8048d54:	55                   	push   ebp
 8048d55:	89 e5                	mov    ebp,esp
 8048d57:	57                   	push   edi
 8048d58:	53                   	push   ebx
 8048d59:	81 ec 30 02 00 00    	sub    esp,0x230
 8048d5f:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8048d62:	89 04 24             	mov    DWORD PTR [esp],eax
 8048d65:	e8 3f ff ff ff       	call   8048ca9 <validate_name>
 8048d6a:	c6 45 f3 00          	mov    BYTE PTR [ebp-0xd],0x0
 8048d6e:	b8 e8 9a 04 08       	mov    eax,0x8049ae8
 8048d73:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
 8048d76:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
 8048d7a:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048d7e:	c7 44 24 04 ff 01 00 	mov    DWORD PTR [esp+0x4],0x1ff
 8048d85:	00 
 8048d86:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048d8c:	89 04 24             	mov    DWORD PTR [esp],eax
 8048d8f:	e8 2c fd ff ff       	call   8048ac0 <snprintf@plt>
 8048d94:	c7 44 24 08 c0 01 00 	mov    DWORD PTR [esp+0x8],0x1c0
 8048d9b:	00 
 8048d9c:	c7 44 24 04 42 02 00 	mov    DWORD PTR [esp+0x4],0x242
 8048da3:	00 
 8048da4:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048daa:	89 04 24             	mov    DWORD PTR [esp],eax
 8048dad:	e8 7e fc ff ff       	call   8048a30 <open@plt>
 8048db2:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 8048db5:	83 7d f4 ff          	cmp    DWORD PTR [ebp-0xc],0xffffffff
 8048db9:	75 40                	jne    8048dfb <background_process+0xa7>
 8048dbb:	e8 10 fd ff ff       	call   8048ad0 <__errno_location@plt>
 8048dc0:	8b 00                	mov    eax,DWORD PTR [eax]
 8048dc2:	89 04 24             	mov    DWORD PTR [esp],eax
 8048dc5:	e8 26 fc ff ff       	call   80489f0 <strerror@plt>
 8048dca:	b9 00 9b 04 08       	mov    ecx,0x8049b00
 8048dcf:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048dd5:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
 8048dd9:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048ddf:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048de3:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8048de7:	89 14 24             	mov    DWORD PTR [esp],edx
 8048dea:	e8 81 fc ff ff       	call   8048a70 <fprintf@plt>
 8048def:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8048df6:	e8 15 fc ff ff       	call   8048a10 <exit@plt>
 8048dfb:	8b 45 10             	mov    eax,DWORD PTR [ebp+0x10]
 8048dfe:	89 85 f0 fd ff ff    	mov    DWORD PTR [ebp-0x210],eax
 8048e04:	8d 85 f0 fd ff ff    	lea    eax,[ebp-0x210]
 8048e0a:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048e0e:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8048e15:	e8 56 fb ff ff       	call   8048970 <setgroups@plt>
 8048e1a:	83 f8 ff             	cmp    eax,0xffffffff
 8048e1d:	75 36                	jne    8048e55 <background_process+0x101>
 8048e1f:	e8 ac fc ff ff       	call   8048ad0 <__errno_location@plt>
 8048e24:	8b 00                	mov    eax,DWORD PTR [eax]
 8048e26:	89 04 24             	mov    DWORD PTR [esp],eax
 8048e29:	e8 c2 fb ff ff       	call   80489f0 <strerror@plt>
 8048e2e:	b9 2c 9b 04 08       	mov    ecx,0x8049b2c
 8048e33:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048e39:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048e3d:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8048e41:	89 14 24             	mov    DWORD PTR [esp],edx
 8048e44:	e8 27 fc ff ff       	call   8048a70 <fprintf@plt>
 8048e49:	c7 04 24 0b 00 00 00 	mov    DWORD PTR [esp],0xb
 8048e50:	e8 bb fb ff ff       	call   8048a10 <exit@plt>
 8048e55:	8b 45 10             	mov    eax,DWORD PTR [ebp+0x10]
 8048e58:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048e5c:	8b 45 10             	mov    eax,DWORD PTR [ebp+0x10]
 8048e5f:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048e63:	8b 45 10             	mov    eax,DWORD PTR [ebp+0x10]
 8048e66:	89 04 24             	mov    DWORD PTR [esp],eax
 8048e69:	e8 e2 fc ff ff       	call   8048b50 <setresgid@plt>
 8048e6e:	83 f8 ff             	cmp    eax,0xffffffff
 8048e71:	75 36                	jne    8048ea9 <background_process+0x155>
 8048e73:	e8 58 fc ff ff       	call   8048ad0 <__errno_location@plt>
 8048e78:	8b 00                	mov    eax,DWORD PTR [eax]
 8048e7a:	89 04 24             	mov    DWORD PTR [esp],eax
 8048e7d:	e8 6e fb ff ff       	call   80489f0 <strerror@plt>
 8048e82:	b9 5c 9b 04 08       	mov    ecx,0x8049b5c
 8048e87:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048e8d:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048e91:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8048e95:	89 14 24             	mov    DWORD PTR [esp],edx
 8048e98:	e8 d3 fb ff ff       	call   8048a70 <fprintf@plt>
 8048e9d:	c7 04 24 0c 00 00 00 	mov    DWORD PTR [esp],0xc
 8048ea4:	e8 67 fb ff ff       	call   8048a10 <exit@plt>
 8048ea9:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 8048eac:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048eb0:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 8048eb3:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048eb7:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 8048eba:	89 04 24             	mov    DWORD PTR [esp],eax
 8048ebd:	e8 2e fa ff ff       	call   80488f0 <setresuid@plt>
 8048ec2:	83 f8 ff             	cmp    eax,0xffffffff
 8048ec5:	75 36                	jne    8048efd <background_process+0x1a9>
 8048ec7:	e8 04 fc ff ff       	call   8048ad0 <__errno_location@plt>
 8048ecc:	8b 00                	mov    eax,DWORD PTR [eax]
 8048ece:	89 04 24             	mov    DWORD PTR [esp],eax
 8048ed1:	e8 1a fb ff ff       	call   80489f0 <strerror@plt>
 8048ed6:	b9 8c 9b 04 08       	mov    ecx,0x8049b8c
 8048edb:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048ee1:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048ee5:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8048ee9:	89 14 24             	mov    DWORD PTR [esp],edx
 8048eec:	e8 7f fb ff ff       	call   8048a70 <fprintf@plt>
 8048ef1:	c7 04 24 0d 00 00 00 	mov    DWORD PTR [esp],0xd
 8048ef8:	e8 13 fb ff ff       	call   8048a10 <exit@plt>
 8048efd:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 8048f04:	00 
 8048f05:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 8048f0c:	e8 af fa ff ff       	call   80489c0 <daemon@plt>
 8048f11:	83 f8 ff             	cmp    eax,0xffffffff
 8048f14:	75 36                	jne    8048f4c <background_process+0x1f8>
 8048f16:	e8 b5 fb ff ff       	call   8048ad0 <__errno_location@plt>
 8048f1b:	8b 00                	mov    eax,DWORD PTR [eax]
 8048f1d:	89 04 24             	mov    DWORD PTR [esp],eax
 8048f20:	e8 cb fa ff ff       	call   80489f0 <strerror@plt>
 8048f25:	b9 bc 9b 04 08       	mov    ecx,0x8049bbc
 8048f2a:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048f30:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048f34:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8048f38:	89 14 24             	mov    DWORD PTR [esp],edx
 8048f3b:	e8 30 fb ff ff       	call   8048a70 <fprintf@plt>
 8048f40:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
 8048f47:	e8 c4 fa ff ff       	call   8048a10 <exit@plt>
 8048f4c:	e8 5f fa ff ff       	call   80489b0 <getpid@plt>
 8048f51:	ba e8 9b 04 08       	mov    edx,0x8049be8
 8048f56:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
 8048f5a:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 8048f5e:	c7 44 24 04 ff 01 00 	mov    DWORD PTR [esp+0x4],0x1ff
 8048f65:	00 
 8048f66:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048f6c:	89 04 24             	mov    DWORD PTR [esp],eax
 8048f6f:	e8 4c fb ff ff       	call   8048ac0 <snprintf@plt>
 8048f74:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048f7a:	c7 85 e4 fd ff ff ff 	mov    DWORD PTR [ebp-0x21c],0xffffffff
 8048f81:	ff ff ff 
 8048f84:	89 c2                	mov    edx,eax
 8048f86:	b8 00 00 00 00       	mov    eax,0x0
 8048f8b:	8b 8d e4 fd ff ff    	mov    ecx,DWORD PTR [ebp-0x21c]
 8048f91:	89 d7                	mov    edi,edx
 8048f93:	f2 ae                	repnz scas al,BYTE PTR es:[edi]
 8048f95:	89 c8                	mov    eax,ecx
 8048f97:	f7 d0                	not    eax
 8048f99:	83 e8 01             	sub    eax,0x1
 8048f9c:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8048fa0:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048fa6:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8048faa:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8048fad:	89 04 24             	mov    DWORD PTR [esp],eax
 8048fb0:	e8 db fa ff ff       	call   8048a90 <write@plt>
 8048fb5:	89 c3                	mov    ebx,eax
 8048fb7:	8d 85 f4 fd ff ff    	lea    eax,[ebp-0x20c]
 8048fbd:	c7 85 e4 fd ff ff ff 	mov    DWORD PTR [ebp-0x21c],0xffffffff
 8048fc4:	ff ff ff 
 8048fc7:	89 c2                	mov    edx,eax
 8048fc9:	b8 00 00 00 00       	mov    eax,0x0
 8048fce:	8b 8d e4 fd ff ff    	mov    ecx,DWORD PTR [ebp-0x21c]
 8048fd4:	89 d7                	mov    edi,edx
 8048fd6:	f2 ae                	repnz scas al,BYTE PTR es:[edi]
 8048fd8:	89 c8                	mov    eax,ecx
 8048fda:	f7 d0                	not    eax
 8048fdc:	83 e8 01             	sub    eax,0x1
 8048fdf:	39 c3                	cmp    ebx,eax
 8048fe1:	74 36                	je     8049019 <background_process+0x2c5>
 8048fe3:	e8 e8 fa ff ff       	call   8048ad0 <__errno_location@plt>
 8048fe8:	8b 00                	mov    eax,DWORD PTR [eax]
 8048fea:	89 04 24             	mov    DWORD PTR [esp],eax
 8048fed:	e8 fe f9 ff ff       	call   80489f0 <strerror@plt>
 8048ff2:	b9 ec 9b 04 08       	mov    ecx,0x8049bec
 8048ff7:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8048ffd:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049001:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8049005:	89 14 24             	mov    DWORD PTR [esp],edx
 8049008:	e8 63 fa ff ff       	call   8048a70 <fprintf@plt>
 804900d:	c7 04 24 03 00 00 00 	mov    DWORD PTR [esp],0x3
 8049014:	e8 f7 f9 ff ff       	call   8048a10 <exit@plt>
 8049019:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 804901c:	89 04 24             	mov    DWORD PTR [esp],eax
 804901f:	e8 3c fb ff ff       	call   8048b60 <close@plt>
 8049024:	83 f8 ff             	cmp    eax,0xffffffff
 8049027:	75 36                	jne    804905f <background_process+0x30b>
 8049029:	e8 a2 fa ff ff       	call   8048ad0 <__errno_location@plt>
 804902e:	8b 00                	mov    eax,DWORD PTR [eax]
 8049030:	89 04 24             	mov    DWORD PTR [esp],eax
 8049033:	e8 b8 f9 ff ff       	call   80489f0 <strerror@plt>
 8049038:	b9 1c 9c 04 08       	mov    ecx,0x8049c1c
 804903d:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8049043:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049047:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 804904b:	89 14 24             	mov    DWORD PTR [esp],edx
 804904e:	e8 1d fa ff ff       	call   8048a70 <fprintf@plt>
 8049053:	c7 04 24 04 00 00 00 	mov    DWORD PTR [esp],0x4
 804905a:	e8 b1 f9 ff ff       	call   8048a10 <exit@plt>
 804905f:	81 c4 30 02 00 00    	add    esp,0x230
 8049065:	5b                   	pop    ebx
 8049066:	5f                   	pop    edi
 8049067:	5d                   	pop    ebp
 8049068:	c3                   	ret    

08049069 <get_tcp_server_socket>:
 8049069:	55                   	push   ebp
 804906a:	89 e5                	mov    ebp,esp
 804906c:	83 ec 48             	sub    esp,0x48
 804906f:	8d 45 e4             	lea    eax,[ebp-0x1c]
 8049072:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
 8049078:	c7 40 04 00 00 00 00 	mov    DWORD PTR [eax+0x4],0x0
 804907f:	c7 40 08 00 00 00 00 	mov    DWORD PTR [eax+0x8],0x0
 8049086:	c7 40 0c 00 00 00 00 	mov    DWORD PTR [eax+0xc],0x0
 804908d:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 8049094:	e8 87 fa ff ff       	call   8048b20 <htonl@plt>
 8049099:	89 45 e8             	mov    DWORD PTR [ebp-0x18],eax
 804909c:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 804909f:	0f b7 c0             	movzx  eax,ax
 80490a2:	89 04 24             	mov    DWORD PTR [esp],eax
 80490a5:	e8 a6 f8 ff ff       	call   8048950 <htons@plt>
 80490aa:	66 89 45 e6          	mov    WORD PTR [ebp-0x1a],ax
 80490ae:	66 c7 45 e4 02 00    	mov    WORD PTR [ebp-0x1c],0x2
 80490b4:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
 80490bb:	00 
 80490bc:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 80490c3:	00 
 80490c4:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
 80490cb:	e8 70 fa ff ff       	call   8048b40 <socket@plt>
 80490d0:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 80490d3:	83 7d f4 ff          	cmp    DWORD PTR [ebp-0xc],0xffffffff
 80490d7:	75 36                	jne    804910f <get_tcp_server_socket+0xa6>
 80490d9:	e8 f2 f9 ff ff       	call   8048ad0 <__errno_location@plt>
 80490de:	8b 00                	mov    eax,DWORD PTR [eax]
 80490e0:	89 04 24             	mov    DWORD PTR [esp],eax
 80490e3:	e8 08 f9 ff ff       	call   80489f0 <strerror@plt>
 80490e8:	b9 48 9c 04 08       	mov    ecx,0x8049c48
 80490ed:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 80490f3:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80490f7:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 80490fb:	89 14 24             	mov    DWORD PTR [esp],edx
 80490fe:	e8 6d f9 ff ff       	call   8048a70 <fprintf@plt>
 8049103:	c7 04 24 05 00 00 00 	mov    DWORD PTR [esp],0x5
 804910a:	e8 01 f9 ff ff       	call   8048a10 <exit@plt>
 804910f:	c7 45 e0 01 00 00 00 	mov    DWORD PTR [ebp-0x20],0x1
 8049116:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
 804911d:	00 
 804911e:	8d 45 e0             	lea    eax,[ebp-0x20]
 8049121:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
 8049125:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 804912c:	00 
 804912d:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 8049134:	00 
 8049135:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049138:	89 04 24             	mov    DWORD PTR [esp],eax
 804913b:	e8 90 f7 ff ff       	call   80488d0 <setsockopt@plt>
 8049140:	83 f8 ff             	cmp    eax,0xffffffff
 8049143:	75 36                	jne    804917b <get_tcp_server_socket+0x112>
 8049145:	e8 86 f9 ff ff       	call   8048ad0 <__errno_location@plt>
 804914a:	8b 00                	mov    eax,DWORD PTR [eax]
 804914c:	89 04 24             	mov    DWORD PTR [esp],eax
 804914f:	e8 9c f8 ff ff       	call   80489f0 <strerror@plt>
 8049154:	b9 78 9c 04 08       	mov    ecx,0x8049c78
 8049159:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 804915f:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049163:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8049167:	89 14 24             	mov    DWORD PTR [esp],edx
 804916a:	e8 01 f9 ff ff       	call   8048a70 <fprintf@plt>
 804916f:	c7 04 24 0a 00 00 00 	mov    DWORD PTR [esp],0xa
 8049176:	e8 95 f8 ff ff       	call   8048a10 <exit@plt>
 804917b:	8d 45 e4             	lea    eax,[ebp-0x1c]
 804917e:	c7 44 24 08 10 00 00 	mov    DWORD PTR [esp+0x8],0x10
 8049185:	00 
 8049186:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 804918a:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 804918d:	89 04 24             	mov    DWORD PTR [esp],eax
 8049190:	e8 0b f9 ff ff       	call   8048aa0 <bind@plt>
 8049195:	83 f8 ff             	cmp    eax,0xffffffff
 8049198:	75 36                	jne    80491d0 <get_tcp_server_socket+0x167>
 804919a:	e8 31 f9 ff ff       	call   8048ad0 <__errno_location@plt>
 804919f:	8b 00                	mov    eax,DWORD PTR [eax]
 80491a1:	89 04 24             	mov    DWORD PTR [esp],eax
 80491a4:	e8 47 f8 ff ff       	call   80489f0 <strerror@plt>
 80491a9:	b9 ac 9c 04 08       	mov    ecx,0x8049cac
 80491ae:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 80491b4:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80491b8:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 80491bc:	89 14 24             	mov    DWORD PTR [esp],edx
 80491bf:	e8 ac f8 ff ff       	call   8048a70 <fprintf@plt>
 80491c4:	c7 04 24 06 00 00 00 	mov    DWORD PTR [esp],0x6
 80491cb:	e8 40 f8 ff ff       	call   8048a10 <exit@plt>
 80491d0:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
 80491d7:	00 
 80491d8:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 80491db:	89 04 24             	mov    DWORD PTR [esp],eax
 80491de:	e8 4d f9 ff ff       	call   8048b30 <listen@plt>
 80491e3:	83 f8 ff             	cmp    eax,0xffffffff
 80491e6:	75 36                	jne    804921e <get_tcp_server_socket+0x1b5>
 80491e8:	e8 e3 f8 ff ff       	call   8048ad0 <__errno_location@plt>
 80491ed:	8b 00                	mov    eax,DWORD PTR [eax]
 80491ef:	89 04 24             	mov    DWORD PTR [esp],eax
 80491f2:	e8 f9 f7 ff ff       	call   80489f0 <strerror@plt>
 80491f7:	b9 dc 9c 04 08       	mov    ecx,0x8049cdc
 80491fc:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8049202:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049206:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 804920a:	89 14 24             	mov    DWORD PTR [esp],edx
 804920d:	e8 5e f8 ff ff       	call   8048a70 <fprintf@plt>
 8049212:	c7 04 24 07 00 00 00 	mov    DWORD PTR [esp],0x7
 8049219:	e8 f2 f7 ff ff       	call   8048a10 <exit@plt>
 804921e:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049221:	c9                   	leave  
 8049222:	c3                   	ret    

08049223 <get_udp_server_socket>:
 8049223:	55                   	push   ebp
 8049224:	89 e5                	mov    ebp,esp
 8049226:	83 ec 48             	sub    esp,0x48
 8049229:	8d 45 e4             	lea    eax,[ebp-0x1c]
 804922c:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
 8049232:	c7 40 04 00 00 00 00 	mov    DWORD PTR [eax+0x4],0x0
 8049239:	c7 40 08 00 00 00 00 	mov    DWORD PTR [eax+0x8],0x0
 8049240:	c7 40 0c 00 00 00 00 	mov    DWORD PTR [eax+0xc],0x0
 8049247:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 804924e:	e8 cd f8 ff ff       	call   8048b20 <htonl@plt>
 8049253:	89 45 e8             	mov    DWORD PTR [ebp-0x18],eax
 8049256:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8049259:	0f b7 c0             	movzx  eax,ax
 804925c:	89 04 24             	mov    DWORD PTR [esp],eax
 804925f:	e8 ec f6 ff ff       	call   8048950 <htons@plt>
 8049264:	66 89 45 e6          	mov    WORD PTR [ebp-0x1a],ax
 8049268:	66 c7 45 e4 02 00    	mov    WORD PTR [ebp-0x1c],0x2
 804926e:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
 8049275:	00 
 8049276:	c7 44 24 04 02 00 00 	mov    DWORD PTR [esp+0x4],0x2
 804927d:	00 
 804927e:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
 8049285:	e8 b6 f8 ff ff       	call   8048b40 <socket@plt>
 804928a:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 804928d:	83 7d f4 ff          	cmp    DWORD PTR [ebp-0xc],0xffffffff
 8049291:	75 36                	jne    80492c9 <get_udp_server_socket+0xa6>
 8049293:	e8 38 f8 ff ff       	call   8048ad0 <__errno_location@plt>
 8049298:	8b 00                	mov    eax,DWORD PTR [eax]
 804929a:	89 04 24             	mov    DWORD PTR [esp],eax
 804929d:	e8 4e f7 ff ff       	call   80489f0 <strerror@plt>
 80492a2:	b9 0c 9d 04 08       	mov    ecx,0x8049d0c
 80492a7:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 80492ad:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80492b1:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 80492b5:	89 14 24             	mov    DWORD PTR [esp],edx
 80492b8:	e8 b3 f7 ff ff       	call   8048a70 <fprintf@plt>
 80492bd:	c7 04 24 05 00 00 00 	mov    DWORD PTR [esp],0x5
 80492c4:	e8 47 f7 ff ff       	call   8048a10 <exit@plt>
 80492c9:	c7 45 e0 01 00 00 00 	mov    DWORD PTR [ebp-0x20],0x1
 80492d0:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
 80492d7:	00 
 80492d8:	8d 45 e0             	lea    eax,[ebp-0x20]
 80492db:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
 80492df:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 80492e6:	00 
 80492e7:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 80492ee:	00 
 80492ef:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 80492f2:	89 04 24             	mov    DWORD PTR [esp],eax
 80492f5:	e8 d6 f5 ff ff       	call   80488d0 <setsockopt@plt>
 80492fa:	83 f8 ff             	cmp    eax,0xffffffff
 80492fd:	75 36                	jne    8049335 <get_udp_server_socket+0x112>
 80492ff:	e8 cc f7 ff ff       	call   8048ad0 <__errno_location@plt>
 8049304:	8b 00                	mov    eax,DWORD PTR [eax]
 8049306:	89 04 24             	mov    DWORD PTR [esp],eax
 8049309:	e8 e2 f6 ff ff       	call   80489f0 <strerror@plt>
 804930e:	b9 3c 9d 04 08       	mov    ecx,0x8049d3c
 8049313:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 8049319:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 804931d:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8049321:	89 14 24             	mov    DWORD PTR [esp],edx
 8049324:	e8 47 f7 ff ff       	call   8048a70 <fprintf@plt>
 8049329:	c7 04 24 0a 00 00 00 	mov    DWORD PTR [esp],0xa
 8049330:	e8 db f6 ff ff       	call   8048a10 <exit@plt>
 8049335:	8d 45 e4             	lea    eax,[ebp-0x1c]
 8049338:	c7 44 24 08 10 00 00 	mov    DWORD PTR [esp+0x8],0x10
 804933f:	00 
 8049340:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049344:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049347:	89 04 24             	mov    DWORD PTR [esp],eax
 804934a:	e8 51 f7 ff ff       	call   8048aa0 <bind@plt>
 804934f:	83 f8 ff             	cmp    eax,0xffffffff
 8049352:	75 36                	jne    804938a <get_udp_server_socket+0x167>
 8049354:	e8 77 f7 ff ff       	call   8048ad0 <__errno_location@plt>
 8049359:	8b 00                	mov    eax,DWORD PTR [eax]
 804935b:	89 04 24             	mov    DWORD PTR [esp],eax
 804935e:	e8 8d f6 ff ff       	call   80489f0 <strerror@plt>
 8049363:	b9 70 9d 04 08       	mov    ecx,0x8049d70
 8049368:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 804936e:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049372:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8049376:	89 14 24             	mov    DWORD PTR [esp],edx
 8049379:	e8 f2 f6 ff ff       	call   8048a70 <fprintf@plt>
 804937e:	c7 04 24 06 00 00 00 	mov    DWORD PTR [esp],0x6
 8049385:	e8 86 f6 ff ff       	call   8048a10 <exit@plt>
 804938a:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 804938d:	c9                   	leave  
 804938e:	c3                   	ret    

0804938f <serve_forever>:
 804938f:	55                   	push   ebp
 8049390:	89 e5                	mov    ebp,esp
 8049392:	83 ec 38             	sub    esp,0x38
 8049395:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8049398:	89 04 24             	mov    DWORD PTR [esp],eax
 804939b:	e8 c9 fc ff ff       	call   8049069 <get_tcp_server_socket>
 80493a0:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 80493a3:	c7 45 dc 10 00 00 00 	mov    DWORD PTR [ebp-0x24],0x10
 80493aa:	8d 55 dc             	lea    edx,[ebp-0x24]
 80493ad:	8d 45 e0             	lea    eax,[ebp-0x20]
 80493b0:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 80493b4:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 80493b8:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 80493bb:	89 04 24             	mov    DWORD PTR [esp],eax
 80493be:	e8 bd f5 ff ff       	call   8048980 <accept@plt>
 80493c3:	89 45 f0             	mov    DWORD PTR [ebp-0x10],eax
 80493c6:	83 7d f0 ff          	cmp    DWORD PTR [ebp-0x10],0xffffffff
 80493ca:	75 36                	jne    8049402 <serve_forever+0x73>
 80493cc:	e8 ff f6 ff ff       	call   8048ad0 <__errno_location@plt>
 80493d1:	8b 00                	mov    eax,DWORD PTR [eax]
 80493d3:	89 04 24             	mov    DWORD PTR [esp],eax
 80493d6:	e8 15 f6 ff ff       	call   80489f0 <strerror@plt>
 80493db:	b9 a0 9d 04 08       	mov    ecx,0x8049da0
 80493e0:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 80493e6:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80493ea:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 80493ee:	89 14 24             	mov    DWORD PTR [esp],edx
 80493f1:	e8 7a f6 ff ff       	call   8048a70 <fprintf@plt>
 80493f6:	c7 04 24 08 00 00 00 	mov    DWORD PTR [esp],0x8
 80493fd:	e8 0e f6 ff ff       	call   8048a10 <exit@plt>
 8049402:	e8 f9 f6 ff ff       	call   8048b00 <fork@plt>
 8049407:	83 f8 ff             	cmp    eax,0xffffffff
 804940a:	74 06                	je     8049412 <serve_forever+0x83>
 804940c:	85 c0                	test   eax,eax
 804940e:	74 38                	je     8049448 <serve_forever+0xb9>
 8049410:	eb 46                	jmp    8049458 <serve_forever+0xc9>
 8049412:	e8 b9 f6 ff ff       	call   8048ad0 <__errno_location@plt>
 8049417:	8b 00                	mov    eax,DWORD PTR [eax]
 8049419:	89 04 24             	mov    DWORD PTR [esp],eax
 804941c:	e8 cf f5 ff ff       	call   80489f0 <strerror@plt>
 8049421:	b9 c8 9d 04 08       	mov    ecx,0x8049dc8
 8049426:	8b 15 c4 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c4
 804942c:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049430:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 8049434:	89 14 24             	mov    DWORD PTR [esp],edx
 8049437:	e8 34 f6 ff ff       	call   8048a70 <fprintf@plt>
 804943c:	c7 04 24 09 00 00 00 	mov    DWORD PTR [esp],0x9
 8049443:	e8 c8 f5 ff ff       	call   8048a10 <exit@plt>
 8049448:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 804944b:	89 04 24             	mov    DWORD PTR [esp],eax
 804944e:	e8 0d f7 ff ff       	call   8048b60 <close@plt>
 8049453:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 8049456:	c9                   	leave  
 8049457:	c3                   	ret    
 8049458:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 804945b:	89 04 24             	mov    DWORD PTR [esp],eax
 804945e:	e8 fd f6 ff ff       	call   8048b60 <close@plt>
 8049463:	90                   	nop
 8049464:	e9 3a ff ff ff       	jmp    80493a3 <serve_forever+0x14>

08049469 <set_io>:
 8049469:	55                   	push   ebp
 804946a:	89 e5                	mov    ebp,esp
 804946c:	83 ec 18             	sub    esp,0x18
 804946f:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 8049476:	00 
 8049477:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 804947a:	89 04 24             	mov    DWORD PTR [esp],eax
 804947d:	e8 5e f4 ff ff       	call   80488e0 <dup2@plt>
 8049482:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
 8049489:	00 
 804948a:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 804948d:	89 04 24             	mov    DWORD PTR [esp],eax
 8049490:	e8 4b f4 ff ff       	call   80488e0 <dup2@plt>
 8049495:	c7 44 24 04 02 00 00 	mov    DWORD PTR [esp+0x4],0x2
 804949c:	00 
 804949d:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 80494a0:	89 04 24             	mov    DWORD PTR [esp],eax
 80494a3:	e8 38 f4 ff ff       	call   80488e0 <dup2@plt>
 80494a8:	a1 c8 b4 04 08       	mov    eax,ds:0x804b4c8
 80494ad:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
 80494b4:	00 
 80494b5:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 80494bc:	00 
 80494bd:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 80494c4:	00 
 80494c5:	89 04 24             	mov    DWORD PTR [esp],eax
 80494c8:	e8 e3 f5 ff ff       	call   8048ab0 <setvbuf@plt>
 80494cd:	a1 e0 b4 04 08       	mov    eax,ds:0x804b4e0
 80494d2:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
 80494d9:	00 
 80494da:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 80494e1:	00 
 80494e2:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 80494e9:	00 
 80494ea:	89 04 24             	mov    DWORD PTR [esp],eax
 80494ed:	e8 be f5 ff ff       	call   8048ab0 <setvbuf@plt>
 80494f2:	a1 c4 b4 04 08       	mov    eax,ds:0x804b4c4
 80494f7:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
 80494fe:	00 
 80494ff:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 8049506:	00 
 8049507:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 804950e:	00 
 804950f:	89 04 24             	mov    DWORD PTR [esp],eax
 8049512:	e8 99 f5 ff ff       	call   8048ab0 <setvbuf@plt>
 8049517:	83 7d 08 02          	cmp    DWORD PTR [ebp+0x8],0x2
 804951b:	7e 0b                	jle    8049528 <set_io+0xbf>
 804951d:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8049520:	89 04 24             	mov    DWORD PTR [esp],eax
 8049523:	e8 38 f6 ff ff       	call   8048b60 <close@plt>
 8049528:	c9                   	leave  
 8049529:	c3                   	ret    

0804952a <restart_process>:
 804952a:	55                   	push   ebp
 804952b:	89 e5                	mov    ebp,esp
 804952d:	83 ec 28             	sub    esp,0x28
 8049530:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8049533:	89 04 24             	mov    DWORD PTR [esp],eax
 8049536:	e8 6e f7 ff ff       	call   8048ca9 <validate_name>
 804953b:	b8 ed 9d 04 08       	mov    eax,0x8049ded
 8049540:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
 8049543:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 8049547:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 804954b:	8d 45 ec             	lea    eax,[ebp-0x14]
 804954e:	89 04 24             	mov    DWORD PTR [esp],eax
 8049551:	e8 8a f5 ff ff       	call   8048ae0 <asprintf@plt>
 8049556:	c7 45 f0 00 9e 04 08 	mov    DWORD PTR [ebp-0x10],0x8049e00
 804955d:	c7 45 f4 00 00 00 00 	mov    DWORD PTR [ebp-0xc],0x0
 8049564:	8b 15 c0 b4 04 08    	mov    edx,DWORD PTR ds:0x804b4c0
 804956a:	8b 45 ec             	mov    eax,DWORD PTR [ebp-0x14]
 804956d:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 8049571:	8d 55 ec             	lea    edx,[ebp-0x14]
 8049574:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
 8049578:	89 04 24             	mov    DWORD PTR [esp],eax
 804957b:	e8 00 f5 ff ff       	call   8048a80 <execve@plt>
 8049580:	e8 4b f5 ff ff       	call   8048ad0 <__errno_location@plt>
 8049585:	8b 00                	mov    eax,DWORD PTR [eax]
 8049587:	89 04 24             	mov    DWORD PTR [esp],eax
 804958a:	e8 61 f4 ff ff       	call   80489f0 <strerror@plt>
 804958f:	8b 4d ec             	mov    ecx,DWORD PTR [ebp-0x14]
 8049592:	ba 09 9e 04 08       	mov    edx,0x8049e09
 8049597:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 804959b:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
 804959f:	89 14 24             	mov    DWORD PTR [esp],edx
 80495a2:	e8 69 f3 ff ff       	call   8048910 <printf@plt>
 80495a7:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 80495ae:	e8 5d f4 ff ff       	call   8048a10 <exit@plt>

080495b3 <is_restarted_process>:
 80495b3:	55                   	push   ebp
 80495b4:	89 e5                	mov    ebp,esp
 80495b6:	57                   	push   edi
 80495b7:	56                   	push   esi
 80495b8:	83 ec 10             	sub    esp,0x10
 80495bb:	83 7d 08 02          	cmp    DWORD PTR [ebp+0x8],0x2
 80495bf:	75 40                	jne    8049601 <is_restarted_process+0x4e>
 80495c1:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 80495c4:	83 c0 04             	add    eax,0x4
 80495c7:	8b 00                	mov    eax,DWORD PTR [eax]
 80495c9:	89 c2                	mov    edx,eax
 80495cb:	b8 00 9e 04 08       	mov    eax,0x8049e00
 80495d0:	b9 09 00 00 00       	mov    ecx,0x9
 80495d5:	89 d6                	mov    esi,edx
 80495d7:	89 c7                	mov    edi,eax
 80495d9:	f3 a6                	repz cmps BYTE PTR ds:[esi],BYTE PTR es:[edi]
 80495db:	0f 97 c2             	seta   dl
 80495de:	0f 92 c0             	setb   al
 80495e1:	89 d1                	mov    ecx,edx
 80495e3:	28 c1                	sub    cl,al
 80495e5:	89 c8                	mov    eax,ecx
 80495e7:	0f be c0             	movsx  eax,al
 80495ea:	85 c0                	test   eax,eax
 80495ec:	75 13                	jne    8049601 <is_restarted_process+0x4e>
 80495ee:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 80495f5:	e8 6f fe ff ff       	call   8049469 <set_io>
 80495fa:	b8 01 00 00 00       	mov    eax,0x1
 80495ff:	eb 05                	jmp    8049606 <is_restarted_process+0x53>
 8049601:	b8 00 00 00 00       	mov    eax,0x0
 8049606:	83 c4 10             	add    esp,0x10
 8049609:	5e                   	pop    esi
 804960a:	5f                   	pop    edi
 804960b:	5d                   	pop    ebp
 804960c:	c3                   	ret    

0804960d <nread>:
 804960d:	55                   	push   ebp
 804960e:	89 e5                	mov    ebp,esp
 8049610:	83 ec 28             	sub    esp,0x28
 8049613:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 8049616:	89 45 ec             	mov    DWORD PTR [ebp-0x14],eax
 8049619:	c7 45 f0 00 00 00 00 	mov    DWORD PTR [ebp-0x10],0x0
 8049620:	c7 45 e8 00 00 00 00 	mov    DWORD PTR [ebp-0x18],0x0
 8049627:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 804962a:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 804962d:	eb 44                	jmp    8049673 <nread+0x66>
 804962f:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 8049632:	8b 55 10             	mov    edx,DWORD PTR [ebp+0x10]
 8049635:	29 c2                	sub    edx,eax
 8049637:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 804963a:	8b 4d ec             	mov    ecx,DWORD PTR [ebp-0x14]
 804963d:	01 c8                	add    eax,ecx
 804963f:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 8049643:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049647:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 804964a:	89 04 24             	mov    DWORD PTR [esp],eax
 804964d:	e8 ae f2 ff ff       	call   8048900 <read@plt>
 8049652:	89 45 e8             	mov    DWORD PTR [ebp-0x18],eax
 8049655:	83 7d e8 00          	cmp    DWORD PTR [ebp-0x18],0x0
 8049659:	7f 0c                	jg     8049667 <nread+0x5a>
 804965b:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8049662:	e8 a9 f3 ff ff       	call   8048a10 <exit@plt>
 8049667:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 804966a:	01 45 f4             	add    DWORD PTR [ebp-0xc],eax
 804966d:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 8049670:	01 45 f0             	add    DWORD PTR [ebp-0x10],eax
 8049673:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 8049676:	3b 45 10             	cmp    eax,DWORD PTR [ebp+0x10]
 8049679:	72 b4                	jb     804962f <nread+0x22>
 804967b:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 804967e:	c9                   	leave  
 804967f:	c3                   	ret    

08049680 <nwrite>:
 8049680:	55                   	push   ebp
 8049681:	89 e5                	mov    ebp,esp
 8049683:	83 ec 28             	sub    esp,0x28
 8049686:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
 8049689:	89 45 ec             	mov    DWORD PTR [ebp-0x14],eax
 804968c:	c7 45 f0 00 00 00 00 	mov    DWORD PTR [ebp-0x10],0x0
 8049693:	c7 45 e8 00 00 00 00 	mov    DWORD PTR [ebp-0x18],0x0
 804969a:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 804969d:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 80496a0:	eb 44                	jmp    80496e6 <nwrite+0x66>
 80496a2:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 80496a5:	8b 55 10             	mov    edx,DWORD PTR [ebp+0x10]
 80496a8:	29 c2                	sub    edx,eax
 80496aa:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 80496ad:	8b 4d ec             	mov    ecx,DWORD PTR [ebp-0x14]
 80496b0:	01 c8                	add    eax,ecx
 80496b2:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
 80496b6:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 80496ba:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 80496bd:	89 04 24             	mov    DWORD PTR [esp],eax
 80496c0:	e8 cb f3 ff ff       	call   8048a90 <write@plt>
 80496c5:	89 45 e8             	mov    DWORD PTR [ebp-0x18],eax
 80496c8:	83 7d e8 00          	cmp    DWORD PTR [ebp-0x18],0x0
 80496cc:	7f 0c                	jg     80496da <nwrite+0x5a>
 80496ce:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 80496d5:	e8 36 f3 ff ff       	call   8048a10 <exit@plt>
 80496da:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 80496dd:	01 45 f4             	add    DWORD PTR [ebp-0xc],eax
 80496e0:	8b 45 e8             	mov    eax,DWORD PTR [ebp-0x18]
 80496e3:	01 45 f0             	add    DWORD PTR [ebp-0x10],eax
 80496e6:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 80496e9:	3b 45 10             	cmp    eax,DWORD PTR [ebp+0x10]
 80496ec:	72 b4                	jb     80496a2 <nwrite+0x22>
 80496ee:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 80496f1:	c9                   	leave  
 80496f2:	c3                   	ret    

080496f3 <secure_srand>:
 80496f3:	55                   	push   ebp
 80496f4:	89 e5                	mov    ebp,esp
 80496f6:	83 ec 28             	sub    esp,0x28
 80496f9:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
 8049700:	00 
 8049701:	c7 04 24 23 9e 04 08 	mov    DWORD PTR [esp],0x8049e23
 8049708:	e8 23 f3 ff ff       	call   8048a30 <open@plt>
 804970d:	89 45 f0             	mov    DWORD PTR [ebp-0x10],eax
 8049710:	83 7d f0 ff          	cmp    DWORD PTR [ebp-0x10],0xffffffff
 8049714:	75 14                	jne    804972a <secure_srand+0x37>
 8049716:	c7 44 24 04 30 9e 04 	mov    DWORD PTR [esp+0x4],0x8049e30
 804971d:	08 
 804971e:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8049725:	e8 36 f2 ff ff       	call   8048960 <err@plt>
 804972a:	c7 44 24 08 04 00 00 	mov    DWORD PTR [esp+0x8],0x4
 8049731:	00 
 8049732:	8d 45 ec             	lea    eax,[ebp-0x14]
 8049735:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049739:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 804973c:	89 04 24             	mov    DWORD PTR [esp],eax
 804973f:	e8 bc f1 ff ff       	call   8048900 <read@plt>
 8049744:	83 f8 04             	cmp    eax,0x4
 8049747:	74 1c                	je     8049765 <secure_srand+0x72>
 8049749:	c7 44 24 08 04 00 00 	mov    DWORD PTR [esp+0x8],0x4
 8049750:	00 
 8049751:	c7 44 24 04 4c 9e 04 	mov    DWORD PTR [esp+0x4],0x8049e4c
 8049758:	08 
 8049759:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 8049760:	e8 fb f1 ff ff       	call   8048960 <err@plt>
 8049765:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
 804976c:	00 
 804976d:	8d 45 ea             	lea    eax,[ebp-0x16]
 8049770:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049774:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 8049777:	89 04 24             	mov    DWORD PTR [esp],eax
 804977a:	e8 81 f1 ff ff       	call   8048900 <read@plt>
 804977f:	83 f8 02             	cmp    eax,0x2
 8049782:	74 1c                	je     80497a0 <secure_srand+0xad>
 8049784:	c7 44 24 08 04 00 00 	mov    DWORD PTR [esp+0x8],0x4
 804978b:	00 
 804978c:	c7 44 24 04 4c 9e 04 	mov    DWORD PTR [esp+0x4],0x8049e4c
 8049793:	08 
 8049794:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 804979b:	e8 c0 f1 ff ff       	call   8048960 <err@plt>
 80497a0:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 80497a3:	89 04 24             	mov    DWORD PTR [esp],eax
 80497a6:	e8 b5 f3 ff ff       	call   8048b60 <close@plt>
 80497ab:	0f b7 45 ea          	movzx  eax,WORD PTR [ebp-0x16]
 80497af:	66 25 ff 07          	and    ax,0x7ff
 80497b3:	66 89 45 ea          	mov    WORD PTR [ebp-0x16],ax
 80497b7:	8b 45 ec             	mov    eax,DWORD PTR [ebp-0x14]
 80497ba:	89 04 24             	mov    DWORD PTR [esp],eax
 80497bd:	e8 7e f2 ff ff       	call   8048a40 <srand@plt>
 80497c2:	c7 45 f4 00 00 00 00 	mov    DWORD PTR [ebp-0xc],0x0
 80497c9:	eb 09                	jmp    80497d4 <secure_srand+0xe1>
 80497cb:	e8 20 f3 ff ff       	call   8048af0 <rand@plt>
 80497d0:	83 45 f4 01          	add    DWORD PTR [ebp-0xc],0x1
 80497d4:	0f b7 45 ea          	movzx  eax,WORD PTR [ebp-0x16]
 80497d8:	0f b7 c0             	movzx  eax,ax
 80497db:	3b 45 f4             	cmp    eax,DWORD PTR [ebp-0xc]
 80497de:	7f eb                	jg     80497cb <secure_srand+0xd8>
 80497e0:	c9                   	leave  
 80497e1:	c3                   	ret    

080497e2 <xmalloc>:
 80497e2:	55                   	push   ebp
 80497e3:	89 e5                	mov    ebp,esp
 80497e5:	83 ec 28             	sub    esp,0x28
 80497e8:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 80497eb:	89 04 24             	mov    DWORD PTR [esp],eax
 80497ee:	e8 ed f1 ff ff       	call   80489e0 <malloc@plt>
 80497f3:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 80497f6:	83 7d f4 00          	cmp    DWORD PTR [ebp-0xc],0x0
 80497fa:	75 14                	jne    8049810 <xmalloc+0x2e>
 80497fc:	c7 44 24 04 76 9e 04 	mov    DWORD PTR [esp+0x4],0x8049e76
 8049803:	08 
 8049804:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
 804980b:	e8 50 f1 ff ff       	call   8048960 <err@plt>
 8049810:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049813:	c9                   	leave  
 8049814:	c3                   	ret    

08049815 <fix_path>:
 8049815:	55                   	push   ebp
 8049816:	89 e5                	mov    ebp,esp
 8049818:	81 ec 98 00 00 00    	sub    esp,0x98
 804981e:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 8049821:	8d 95 78 ff ff ff    	lea    edx,[ebp-0x88]
 8049827:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
 804982b:	89 04 24             	mov    DWORD PTR [esp],eax
 804982e:	e8 ed f1 ff ff       	call   8048a20 <realpath@plt>
 8049833:	85 c0                	test   eax,eax
 8049835:	75 07                	jne    804983e <fix_path+0x29>
 8049837:	b8 01 00 00 00       	mov    eax,0x1
 804983c:	eb 15                	jmp    8049853 <fix_path+0x3e>
 804983e:	8d 85 78 ff ff ff    	lea    eax,[ebp-0x88]
 8049844:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049848:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
 804984b:	89 04 24             	mov    DWORD PTR [esp],eax
 804984e:	e8 4d f1 ff ff       	call   80489a0 <strcpy@plt>
 8049853:	c9                   	leave  
 8049854:	c3                   	ret    

08049855 <parse_http_request>:
 8049855:	55                   	push   ebp
 8049856:	89 e5                	mov    ebp,esp
 8049858:	57                   	push   edi
 8049859:	56                   	push   esi
 804985a:	81 ec 20 04 00 00    	sub    esp,0x420
 8049860:	b8 84 9e 04 08       	mov    eax,0x8049e84
 8049865:	8d 95 f0 fb ff ff    	lea    edx,[ebp-0x410]
 804986b:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
 804986f:	89 04 24             	mov    DWORD PTR [esp],eax
 8049872:	e8 99 f0 ff ff       	call   8048910 <printf@plt>
 8049877:	c7 44 24 08 00 04 00 	mov    DWORD PTR [esp+0x8],0x400
 804987e:	00 
 804987f:	8d 85 f0 fb ff ff    	lea    eax,[ebp-0x410]
 8049885:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049889:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 8049890:	e8 6b f0 ff ff       	call   8048900 <read@plt>
 8049895:	85 c0                	test   eax,eax
 8049897:	7f 14                	jg     80498ad <parse_http_request+0x58>
 8049899:	c7 44 24 04 a8 9e 04 	mov    DWORD PTR [esp+0x4],0x8049ea8
 80498a0:	08 
 80498a1:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 80498a8:	e8 63 f2 ff ff       	call   8048b10 <errx@plt>
 80498ad:	c7 44 24 08 04 00 00 	mov    DWORD PTR [esp+0x8],0x4
 80498b4:	00 
 80498b5:	c7 44 24 04 c8 9e 04 	mov    DWORD PTR [esp+0x4],0x8049ec8
 80498bc:	08 
 80498bd:	8d 85 f0 fb ff ff    	lea    eax,[ebp-0x410]
 80498c3:	89 04 24             	mov    DWORD PTR [esp],eax
 80498c6:	e8 65 f0 ff ff       	call   8048930 <memcmp@plt>
 80498cb:	85 c0                	test   eax,eax
 80498cd:	74 14                	je     80498e3 <parse_http_request+0x8e>
 80498cf:	c7 44 24 04 cd 9e 04 	mov    DWORD PTR [esp+0x4],0x8049ecd
 80498d6:	08 
 80498d7:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 80498de:	e8 2d f2 ff ff       	call   8048b10 <errx@plt>
 80498e3:	8d 85 f0 fb ff ff    	lea    eax,[ebp-0x410]
 80498e9:	83 c0 04             	add    eax,0x4
 80498ec:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
 80498ef:	c7 44 24 04 20 00 00 	mov    DWORD PTR [esp+0x4],0x20
 80498f6:	00 
 80498f7:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 80498fa:	89 04 24             	mov    DWORD PTR [esp],eax
 80498fd:	e8 4e f1 ff ff       	call   8048a50 <strchr@plt>
 8049902:	89 45 f0             	mov    DWORD PTR [ebp-0x10],eax
 8049905:	83 7d f0 00          	cmp    DWORD PTR [ebp-0x10],0x0
 8049909:	75 14                	jne    804991f <parse_http_request+0xca>
 804990b:	c7 44 24 04 df 9e 04 	mov    DWORD PTR [esp+0x4],0x8049edf
 8049912:	08 
 8049913:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 804991a:	e8 f1 f1 ff ff       	call   8048b10 <errx@plt>
 804991f:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 8049922:	c6 00 00             	mov    BYTE PTR [eax],0x0
 8049925:	83 45 f0 01          	add    DWORD PTR [ebp-0x10],0x1
 8049929:	8b 45 f0             	mov    eax,DWORD PTR [ebp-0x10]
 804992c:	89 c2                	mov    edx,eax
 804992e:	b8 fd 9e 04 08       	mov    eax,0x8049efd
 8049933:	b9 08 00 00 00       	mov    ecx,0x8
 8049938:	89 d6                	mov    esi,edx
 804993a:	89 c7                	mov    edi,eax
 804993c:	f3 a6                	repz cmps BYTE PTR ds:[esi],BYTE PTR es:[edi]
 804993e:	0f 97 c2             	seta   dl
 8049941:	0f 92 c0             	setb   al
 8049944:	89 d1                	mov    ecx,edx
 8049946:	28 c1                	sub    cl,al
 8049948:	89 c8                	mov    eax,ecx
 804994a:	0f be c0             	movsx  eax,al
 804994d:	85 c0                	test   eax,eax
 804994f:	74 14                	je     8049965 <parse_http_request+0x110>
 8049951:	c7 44 24 04 06 9f 04 	mov    DWORD PTR [esp+0x4],0x8049f06
 8049958:	08 
 8049959:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
 8049960:	e8 ab f1 ff ff       	call   8048b10 <errx@plt>
 8049965:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049968:	89 04 24             	mov    DWORD PTR [esp],eax
 804996b:	e8 a5 fe ff ff       	call   8049815 <fix_path>
 8049970:	b8 17 9f 04 08       	mov    eax,0x8049f17
 8049975:	8b 55 f4             	mov    edx,DWORD PTR [ebp-0xc]
 8049978:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
 804997c:	89 04 24             	mov    DWORD PTR [esp],eax
 804997f:	e8 8c ef ff ff       	call   8048910 <printf@plt>
 8049984:	8b 45 f4             	mov    eax,DWORD PTR [ebp-0xc]
 8049987:	81 c4 20 04 00 00    	add    esp,0x420
 804998d:	5e                   	pop    esi
 804998e:	5f                   	pop    edi
 804998f:	5d                   	pop    ebp
 8049990:	c3                   	ret    

08049991 <main>:
 8049991:	55                   	push   ebp
 8049992:	89 e5                	mov    ebp,esp
 8049994:	83 e4 f0             	and    esp,0xfffffff0
 8049997:	83 ec 20             	sub    esp,0x20
 804999a:	c7 44 24 08 20 4e 00 	mov    DWORD PTR [esp+0x8],0x4e20
 80499a1:	00 
 80499a2:	c7 44 24 04 20 4e 00 	mov    DWORD PTR [esp+0x4],0x4e20
 80499a9:	00 
 80499aa:	c7 04 24 2c 9f 04 08 	mov    DWORD PTR [esp],0x8049f2c
 80499b1:	e8 9e f3 ff ff       	call   8048d54 <background_process>
 80499b6:	c7 04 24 20 4e 00 00 	mov    DWORD PTR [esp],0x4e20
 80499bd:	e8 cd f9 ff ff       	call   804938f <serve_forever>
 80499c2:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
 80499c6:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
 80499ca:	89 04 24             	mov    DWORD PTR [esp],eax
 80499cd:	e8 97 fa ff ff       	call   8049469 <set_io>
 80499d2:	e8 7e fe ff ff       	call   8049855 <parse_http_request>
 80499d7:	c9                   	leave  
 80499d8:	c3                   	ret    
 80499d9:	90                   	nop
 80499da:	90                   	nop
 80499db:	90                   	nop
 80499dc:	90                   	nop
 80499dd:	90                   	nop
 80499de:	90                   	nop
 80499df:	90                   	nop

080499e0 <__libc_csu_init>:
 80499e0:	55                   	push   ebp
 80499e1:	57                   	push   edi
 80499e2:	56                   	push   esi
 80499e3:	53                   	push   ebx
 80499e4:	e8 69 00 00 00       	call   8049a52 <__i686.get_pc_thunk.bx>
 80499e9:	81 c3 03 1a 00 00    	add    ebx,0x1a03
 80499ef:	83 ec 1c             	sub    esp,0x1c
 80499f2:	8b 6c 24 30          	mov    ebp,DWORD PTR [esp+0x30]
 80499f6:	8d bb 10 ff ff ff    	lea    edi,[ebx-0xf0]
 80499fc:	e8 8b ee ff ff       	call   804888c <_init>
 8049a01:	8d 83 08 ff ff ff    	lea    eax,[ebx-0xf8]
 8049a07:	29 c7                	sub    edi,eax
 8049a09:	c1 ff 02             	sar    edi,0x2
 8049a0c:	85 ff                	test   edi,edi
 8049a0e:	74 29                	je     8049a39 <__libc_csu_init+0x59>
 8049a10:	31 f6                	xor    esi,esi
 8049a12:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
 8049a18:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
 8049a1c:	89 2c 24             	mov    DWORD PTR [esp],ebp
 8049a1f:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 8049a23:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
 8049a27:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
 8049a2b:	ff 94 b3 08 ff ff ff 	call   DWORD PTR [ebx+esi*4-0xf8]
 8049a32:	83 c6 01             	add    esi,0x1
 8049a35:	39 fe                	cmp    esi,edi
 8049a37:	75 df                	jne    8049a18 <__libc_csu_init+0x38>
 8049a39:	83 c4 1c             	add    esp,0x1c
 8049a3c:	5b                   	pop    ebx
 8049a3d:	5e                   	pop    esi
 8049a3e:	5f                   	pop    edi
 8049a3f:	5d                   	pop    ebp
 8049a40:	c3                   	ret    
 8049a41:	eb 0d                	jmp    8049a50 <__libc_csu_fini>
 8049a43:	90                   	nop
 8049a44:	90                   	nop
 8049a45:	90                   	nop
 8049a46:	90                   	nop
 8049a47:	90                   	nop
 8049a48:	90                   	nop
 8049a49:	90                   	nop
 8049a4a:	90                   	nop
 8049a4b:	90                   	nop
 8049a4c:	90                   	nop
 8049a4d:	90                   	nop
 8049a4e:	90                   	nop
 8049a4f:	90                   	nop

08049a50 <__libc_csu_fini>:
 8049a50:	f3 c3                	repz ret 

08049a52 <__i686.get_pc_thunk.bx>:
 8049a52:	8b 1c 24             	mov    ebx,DWORD PTR [esp]
 8049a55:	c3                   	ret    
 8049a56:	90                   	nop
 8049a57:	90                   	nop
 8049a58:	90                   	nop
 8049a59:	90                   	nop
 8049a5a:	90                   	nop
 8049a5b:	90                   	nop
 8049a5c:	90                   	nop
 8049a5d:	90                   	nop
 8049a5e:	90                   	nop
 8049a5f:	90                   	nop

08049a60 <__do_global_ctors_aux>:
 8049a60:	55                   	push   ebp
 8049a61:	89 e5                	mov    ebp,esp
 8049a63:	53                   	push   ebx
 8049a64:	83 ec 04             	sub    esp,0x4
 8049a67:	a1 fc b2 04 08       	mov    eax,ds:0x804b2fc
 8049a6c:	83 f8 ff             	cmp    eax,0xffffffff
 8049a6f:	74 13                	je     8049a84 <__do_global_ctors_aux+0x24>
 8049a71:	bb fc b2 04 08       	mov    ebx,0x804b2fc
 8049a76:	66 90                	xchg   ax,ax
 8049a78:	83 eb 04             	sub    ebx,0x4
 8049a7b:	ff d0                	call   eax
 8049a7d:	8b 03                	mov    eax,DWORD PTR [ebx]
 8049a7f:	83 f8 ff             	cmp    eax,0xffffffff
 8049a82:	75 f4                	jne    8049a78 <__do_global_ctors_aux+0x18>
 8049a84:	83 c4 04             	add    esp,0x4
 8049a87:	5b                   	pop    ebx
 8049a88:	5d                   	pop    ebp
 8049a89:	c3                   	ret    
 8049a8a:	90                   	nop
 8049a8b:	90                   	nop

Disassembly of section .fini:

08049a8c <_fini>:
 8049a8c:	53                   	push   ebx
 8049a8d:	83 ec 08             	sub    esp,0x8
 8049a90:	e8 00 00 00 00       	call   8049a95 <_fini+0x9>
 8049a95:	5b                   	pop    ebx
 8049a96:	81 c3 57 19 00 00    	add    ebx,0x1957
 8049a9c:	e8 ff f0 ff ff       	call   8048ba0 <__do_global_dtors_aux>
 8049aa1:	83 c4 08             	add    esp,0x8
 8049aa4:	5b                   	pop    ebx
 8049aa5:	c3                   	ret    
