	.file	"macro.cpp"
	.section	.rodata
.LC0:
	.string	"macro.cpp"
.LC1:
	.string	"func: %s, line: %d, file:%s\n"
	.text
.globl _Z3foov
	.type	_Z3foov, @function
_Z3foov:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	movl	$.LC0, %ecx
	movl	$5, %edx
	movl	$_ZZ3foovE12__FUNCTION__, %esi
	movl	$.LC1, %edi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	_Z3foov, .-_Z3foov
	.section	.rodata
.LC2:
	.string	"func: %s\n"
	.text
.globl _Z9printFuncPKc
	.type	_Z9printFuncPKc, @function
_Z9printFuncPKc:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movq	%rax, %rsi
	movl	$.LC2, %edi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	_Z9printFuncPKc, .-_Z9printFuncPKc
	.section	.rodata
.LC3:
	.string	"file: %s\n"
	.text
.globl _Z9printFilePKc
	.type	_Z9printFilePKc, @function
_Z9printFilePKc:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movq	%rax, %rsi
	movl	$.LC3, %edi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	_Z9printFilePKc, .-_Z9printFilePKc
.globl main
	.type	main, @function
main:
.LFB3:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	movl	$.LC0, %ecx
	movl	$20, %edx
	movl	$_ZZ4mainE12__FUNCTION__, %esi
	movl	$.LC1, %edi
	movl	$0, %eax
	call	printf
	call	_Z3foov
	movl	$_ZZ4mainE12__FUNCTION__, %edi
	call	_Z9printFuncPKc
	movl	$.LC0, %edi
	call	_Z9printFilePKc
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
	.size	main, .-main
	.section	.rodata
	.type	_ZZ4mainE12__FUNCTION__, @object
	.size	_ZZ4mainE12__FUNCTION__, 5
_ZZ4mainE12__FUNCTION__:
	.string	"main"
	.type	_ZZ3foovE12__FUNCTION__, @object
	.size	_ZZ3foovE12__FUNCTION__, 4
_ZZ3foovE12__FUNCTION__:
	.string	"foo"
	.ident	"GCC: (Gentoo 4.5.3-r2 p1.5, pie-0.4.7) 4.5.3"
	.section	.note.GNU-stack,"",@progbits
