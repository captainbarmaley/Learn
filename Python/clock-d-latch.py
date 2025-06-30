import time

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

    return Q, Qi


# 2 ВЫХОДА - СВЯЗАННЫ ОБРАТНОЙ СВЯЗЬЮ
Q = 0
Qi = 1
CLOCK = 0

while True:
    # 2 ВХОДА ДАННЫЕ И СИГНАЛ ЗАПИСИ
    DATA = int(input("DATA: "))
    CLOCK = 1 - CLOCK
    print("-"*30)

    # ПРОВЕРКА НА ВВОД
    if DATA not in (0, 1):
        print("ERROR! INPUT MUST BE 1 OR 0\n")
        continue

    # ЗАПУСКАЕМ D-TRIGGER
    Q, Qi = UPDATE_D_LATCH(DATA, CLOCK, Q, Qi)

    print(f"\nDATA = {DATA}, CLOCK = {CLOCK} --> Q = {Q}, Qi = {Qi}")
    time.sleep(1)
