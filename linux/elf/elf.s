	.file	"elf.c"
	.comm	big_big_array,41943040,64
	.globl	a_string
	.section	.rodata
.LC0:
	.string	"hello world!"
	.data
	.align 8
	.type	a_string, @object
	.size	a_string, 8
a_string:
	.quad	.LC0
	.globl	a_global_var_with_value
	.align 4
	.type	a_global_var_with_value, @object
	.size	a_global_var_with_value, 4
a_global_var_with_value:
	.long	256
	.comm	a_global_val_without_value,4,4
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$512, -4(%rbp)
	movl	$768, big_big_array(%rip)
	movq	a_string(%rip), %rax
	movq	%rax, %rdi
	call	puts
	movl	a_global_var_with_value(%rip), %eax
	addl	$1, %eax
	movl	%eax, a_global_var_with_value(%rip)
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.9.1-16ubuntu6) 4.9.1"
	.section	.note.GNU-stack,"",@progbits
