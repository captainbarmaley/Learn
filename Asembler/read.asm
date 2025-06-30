section .bss ; секция неиницилизированных данных
    buffer resb 128 ; выделяем 128 байтов под ввод

section .data
    greet_msg db 'Input text and I will repeat it: '
    len equ $ - greet_msg

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, greet_msg
    mov rdx, len
    syscall

    ; Читаем данные (syscall: read)
    mov rax, 0 ; режим чтения
    mov rdi, 0 ; stdin

    mov rsi, buffer ; куда сохранять
    mov rdx, 128
    syscall

    ;Сохраняем количество прочитанных байт (те что в RAX)
    mov rdx, rax ; rdx = сколько прочитано

    ;Выводим обратно
    mov rax, 1
    mov rdi, 1

    mov rsi, buffer
    syscall

    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall
