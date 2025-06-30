def UPDATE_D_LATCH(DATA, ENABLE, Q, Qi):
    def NOR(a, b):
        return 1 - (a | b)

    def NOT(a):
        return 1 - a

    def AND(a, b):
        return a & b

    # ЛОГИКА ПРЕОБРАЗОВАНИЯ 
    SET = AND(DATA, ENABLE) # УСТАНОВКА РАВНА 1 ЕСЛИ ДАННЫЕ И СИГНАЛ РАВНЫ 1
    RESET = AND(NOT(DATA), ENABLE) # СБРОС РАВЕН 1 ЕСЛИ ИНВЕРТИРОВАННЫЕ ДАННЫЕ И СИГНАЛ РАВНЫ 1

    # ИТЕРАЦИЯ 5 РАЗ ДЛЯ УСТАКАНИВАНИЯ СИГНАЛА
    for _ in range(5):
        # ВЫЧИСЛЕНИЕ Q И Qi
        Q_next = NOR(RESET, Qi) # НА ВЫХОД 1 ЕСЛИ СБРОС И Qi РАВНЫ 0 } ИНАЧЕ НА ВЫХОД 0
        Qi_next = NOR(Q, SET) # НА ВЫХОД 1 ЕСЛИ Q И УСТАНОВКА РАВНЫ 0 } ИНАЧЕ НА ВЫХОД 0
        Q = Q_next
        Qi = Qi_next

    return Q, Qi, SET, RESET


# 2 ВЫХОДА - СВЯЗАННЫ ОБРАТНОЙ СВЯЗЬЮ
Q = 0
Qi = 1

while True:
    # 2 ВХОДА ДАННЫЕ И СИГНАЛ ЗАПИСИ
    DATA = int(input("DATA: "))
    ENABLE = int(input("ENABLE (1 - WRITE / 0 - HOLD): "))
    print("-"*30)

    # ПРОВЕРКА НА ВВОД
    if DATA not in (0, 1) or ENABLE not in (0, 1):
        print("ERROR! INPUT MUST BE 1 OR 0\n")
        continue

    # ЗАПУСКАЕМ D-TRIGGER
    Q, Qi, SET, RESET = UPDATE_D_LATCH(DATA, ENABLE, Q, Qi)

    # ПОЯСНЕНИЯ
    if SET == 1 and RESET == 0:
        print("-> SET")
    elif SET == 0 and RESET == 1:
        print("-> RESET")
    elif SET == 0 and RESET == 0:
        print("-> HOLD")

    print(f"\nDATA = {DATA}, ENABLE = {ENABLE} --> Q = {Q}, Qi = {Qi}")
