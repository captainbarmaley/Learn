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
T = 1
TICK = 0
Q = 0
Qi = 1
CLOCK = 0

while True:
    # ОДИН ВХОД - ПЕРЕКЛЮЧАТЕЛЬ
    
    CLOCK = 1 - CLOCK

    ENABLE = (T & CLOCK) # ВКЛЮЧАЕМ ЗАПИСЬ ЕСЛИ Т = 1
    DATA = Qi # ПОДАЕМ ИНВЕРСНОЕ Q

    print("-"*30)

    # ПРОВЕРКА НА ВВОД
    if T not in (0, 1):
        print("ERROR! INPUT MUST BE 1 OR 0\n")
        continue

    # ЗАПУСКАЕМ D-TRIGGER
    Q, Qi = UPDATE_D_LATCH(DATA, ENABLE, Q, Qi)

    # ПОЯСНЕНИЯ
    if ENABLE == 0:
        print("-> HOLD")
    elif ENABLE == 1:
        print("-> TOGGLE")

    TICK += 1
    print(f"\n[{TICK}] TOGGLE = {T} --> Q = {Q}, Qi = {Qi}")
    time.sleep(1)
