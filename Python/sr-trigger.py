# 2 ВЫХОДА - СВЯЗАННЫ ОБРАТНОЙ СВЯЗЬЮ
Q = 0
Qi = 1

def NOR(a, b):
    return 1 - (a | b)

def NOT(a):
    return 1 - a


while True:
    # 2 ВХОДА УСТАНОВКА И СБРОС
    S = int(input("\nSET BIT: "))
    R = int(input("RESET ENABLE: "))
    print("-"*30)

    # ИТЕРАЦИЯ 5 РАЗ ДЛЯ УСТАКАНИВАНИЯ СИГНАЛА
    for _ in range(5):
        # ВЫЧИСЛЕНИЕ Q И Qi
        Q_next = NOR(R, Qi) # НА ВЫХОД 1 ЕСЛИ СБРОС И Qi РАВНЫ 0 } ИНАЧЕ НА ВЫХОД 0
        Qi_next = NOR(Q, S) # НА ВЫХОД 1 ЕСЛИ Q И УСТАНОВКА РАВНЫ 0 } ИНАЧЕ НА ВЫХОД 0
        Q = Q_next
        Qi = Qi_next

    # ПОЯСНЕНИЯ
    if S == 1 and R == 0:
        print("-> SET")
    elif S == 0 and R == 1:
        print("-> RESET")
    elif S == 0 and R == 0:
        print("-> HOLD")
    elif S == 1 and R == 1:
        print("-> ERROR - WRONG INPUT")

    print(f"\nSET: {S} | RESET: {R} | Q: {Q} | Qi: {Qi}")
