; Данные
section .data
    hello_msg db 'Hello, world', 0xA ; Строка для вывода, '\n' и null-терминатор
    len_msg equ $ - hello_msg ; Длинна строки

; Код
section .text
    global _start ; Точка входа в программу

_start:
    ;Выводим строку на экран
    mov rax, 1 ; syscall 1 - write
    mov rdi, 1 ; Дискриптор 1 - stdout
    mov rsi, hello_msg ; Адрес строки для вывода
    mov rdx, len_msg ; Длинна строки
    syscall ; Вызов системного вызова

    ;Завершение программы
    mov rax, 60 ; Системный вызов для выхода
    xor rdi, rdi ; Код возврата = 0
    syscall
