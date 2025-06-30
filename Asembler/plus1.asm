section .bss
    input resb 32
    output resb 32

section .text
    global _start

_start:
    ; Read Input
    mov rax, 0
    mov rdi, 0
    mov rsi, input
    mov rdx, 32
    syscall

    mov rcx, rax ; rcx = len of line

    ; String -> Integer
    xor rbx, rbx ; int = 0
    xor rsi, rsi ; index = 0

.parse_loop:
    mov al, [input + rsi] ; al = current char
    cmp al, 10 ; its '\n'?
    je .done_parse ; if 'yes' - end of input
    sub al, '0' ; ASCII -> Integer
    imul rbx, rbx, 10 ; int *= 10
    add rbx, rax ; int += int
    inc rsi ; next char
    jmp .parse_loop

.done_parse:
    ; +1
    add rbx, 1 ; int++

    ; Int -> String
    mov rsi, output + 31 ; pointer in the end of buffer
    mov byte [rsi], 10 ; '\n'
    dec rsi

.convert_loop:
    xor rdx, rdx
    mov rax, rbx
    mov r10, 10
    div r10 ; rax = rbx / 10, rdx = rbx % 10
    add dl, '0' ; ASCII int
    mov [rsi], dl
    dec rsi
    mov rbx, rax
    test rax, rax
    jnz .convert_loop

    inc rsi ; rsi -> start of line

    ; Print of result

    mov rax, 1
    mov rdi, 1
    mov rdx, output + 32
    sub rdx, rsi
    syscall

    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall
