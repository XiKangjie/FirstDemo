	.file	"thread_local.cpp"
	.section	.text._ZN3Foo11GetInstanceEv,"axG",@progbits,_ZN3Foo11GetInstanceEv,comdat
	.weak	_ZN3Foo11GetInstanceEv
	.type	_ZN3Foo11GetInstanceEv, @function
_ZN3Foo11GetInstanceEv:
.LFB9:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	movl	$_ZZN3Foo11GetInstanceEvE1f, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE9:
	.size	_ZN3Foo11GetInstanceEv, .-_ZN3Foo11GetInstanceEv
.globl _ZN3Foo3valE
	.section	.tbss,"awT",@nobits
	.align 4
	.type	_ZN3Foo3valE, @object
	.size	_ZN3Foo3valE, 4
_ZN3Foo3valE:
	.zero	4
	.section	.rodata
.LC0:
	.string	"tfun1: %d\n"
	.text
.globl _Z5tfun1Pv
	.type	_Z5tfun1Pv, @function
_Z5tfun1Pv:
.LFB10:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	call	_ZN3Foo11GetInstanceEv
	movl	%fs:_ZN3Foo3valE@tpoff, %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	call	_ZN3Foo11GetInstanceEv
	movl	$1, %fs:_ZN3Foo3valE@tpoff
	call	_ZN3Foo11GetInstanceEv
	movl	%fs:_ZN3Foo3valE@tpoff, %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE10:
	.size	_Z5tfun1Pv, .-_Z5tfun1Pv
	.section	.rodata
.LC1:
	.string	"tfun2: %d\n"
	.text
.globl _Z5tfun2Pv
	.type	_Z5tfun2Pv, @function
_Z5tfun2Pv:
.LFB11:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	call	_ZN3Foo11GetInstanceEv
	movl	%fs:_ZN3Foo3valE@tpoff, %eax
	movl	%eax, %esi
	movl	$.LC1, %edi
	movl	$0, %eax
	call	printf
	call	_ZN3Foo11GetInstanceEv
	movl	$2, %fs:_ZN3Foo3valE@tpoff
	call	_ZN3Foo11GetInstanceEv
	movl	%fs:_ZN3Foo3valE@tpoff, %eax
	movl	%eax, %esi
	movl	$.LC1, %edi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE11:
	.size	_Z5tfun2Pv, .-_Z5tfun2Pv
.globl main
	.type	main, @function
main:
.LFB12:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	movq	%rsp, %rbp
	.cfi_offset 6, -16
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	leaq	-8(%rbp), %rax
	movl	$0, %ecx
	movl	$_Z5tfun1Pv, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_create
	movl	$1, %edi
	call	sleep
	leaq	-16(%rbp), %rax
	movl	$0, %ecx
	movl	$_Z5tfun2Pv, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_create
	movq	-8(%rbp), %rax
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_join
	movq	-16(%rbp), %rax
	movl	$0, %esi
	movq	%rax, %rdi
	call	pthread_join
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE12:
	.size	main, .-main
	.weak	_ZZN3Foo11GetInstanceEvE1f
	.section	.bss._ZZN3Foo11GetInstanceEvE1f,"awG",@nobits,_ZZN3Foo11GetInstanceEvE1f,comdat
	.type	_ZZN3Foo11GetInstanceEvE1f, @gnu_unique_object
	.size	_ZZN3Foo11GetInstanceEvE1f, 1
_ZZN3Foo11GetInstanceEvE1f:
	.zero	1
	.ident	"GCC: (Gentoo 4.5.3-r2 p1.5, pie-0.4.7) 4.5.3"
	.section	.note.GNU-stack,"",@progbits
