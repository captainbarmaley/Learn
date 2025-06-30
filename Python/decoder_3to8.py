def NOT(a): return 1 - a # Инвертируем бит (0 -> 1, 1 -> 0)
def AND(a, b, c): return a & b & c # Побитовая операция AND для трех входов

# Дешифратор
def decoder3to8(A2, A1, A0):
    # Каждый вход активен только при уникальной комбинации входов
    Y0 = AND(NOT(A2), NOT(A1), NOT(A0))
    Y1 = AND(NOT(A2), NOT(A1),     A0)
    Y2 = AND(NOT(A2),     A1,  NOT(A0))
    Y3 = AND(NOT(A2),     A1,      A0)
    Y4 = AND(    A2,  NOT(A1), NOT(A0))
    Y5 = AND(    A2,  NOT(A1),     A0)
    Y6 = AND(    A2,      A1,  NOT(A0))
    Y7 = AND(    A2,      A1,      A0)
    
    return Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7

# Цикл проверки
for A2 in [0, 1]:
    for A1 in [0, 1]:
        for A0 in [0, 1]:
            Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7 = decoder3to8(A2, A1, A0)
            print(f"A2:{A2}, A1:{A1}, A0:{A0} ---> {Y0}-{Y1}-{Y2}-{Y3}-{Y4}-{Y5}-{Y6}-{Y7}")
