section .text
    global _start

_start:
    mov rdi, 42; код возврата = 42 (в RDI)
    mov rax, 60; системный вызов 'exit' (номер 60)
    syscall ; вызвать системный вызов (завершение)
