section .data
    first_msg db 'Hello '
    second_msg db 'world', 0xA
    len equ $ - first_msg
    s_len equ $ - second_msg

section .text
    global _start

_start:
    
    mov rax, 1
    mov rdi, 1

    mov rsi, first_msg
    mov rdx, len
    
    syscall

    mov rsi, second_msg
    mov rdx, s_len

    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
