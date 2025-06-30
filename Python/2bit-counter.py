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
T1 = 1
TICK = 0
Q1, Q2 = 0, 0
Qi1, Qi2 = 1, 1
CLOCK = 0

while True:
    # 
    CLOCK = 1 - CLOCK

    # ЗАПУСКАЕМ D-TRIGGER
    Q1, Qi1 = UPDATE_D_LATCH(Qi1, CLOCK & 1, Q1, Qi1)
    Q2, Qi2 = UPDATE_D_LATCH(Qi2, CLOCK & Q1, Q2, Qi2)

    TICK += 1
    print(f"\n[{TICK}] Q1 = {Q1} | Q2 = {Q2} | CLOCK = {CLOCK} --> Q = {Q2}, Qi = {Qi2}")
    time.sleep(1)
