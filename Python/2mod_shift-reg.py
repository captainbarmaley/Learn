import time

# D-триггер на SR-защелке
def update_dlatch(D, E, Q, Qi):
    def NOR(a, b): return 1 - (a | b)
    def NOT(a): return 1 - a
    def AND(a, b): return a & b

    S = AND(D, E)
    R = AND(NOT(D), E)

    for _ in range(5):
        Q_next = NOR(R, Qi)
        Qi_next = NOR(S, Q)
        Q = Q_next
        Qi = Qi_next

    return Q, Qi

# Один бит регистра с LOAD и SHIFT
def reg_bit(IN, LEFT, RIGHT, LOAD, SHIFT, CLK, Q, Qi):
    if LOAD:
        D = IN
    else:
        D = RIGHT if SHIFT else LEFT
    return update_dlatch(D, CLK, Q, Qi)

# Регистр из 4-х бит
Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1
Q3, Qi3 = 0, 1

# Входные данные
IN = [1, 0, 1, 0]  # IN0 IN1 IN2 IN3

# Сигналы загрузки и сдвига
LOAD = 1
SHIFT = 1  # 1 — вправо, 0 — влево
first = True
CLK = 0

# Работа регистра
for tick in range(10):
    CLK = 1 - CLK

    if CLK == 1:
        # Сохраняем предыдущие значения — очень важно!
        prev_Q0, prev_Q1, prev_Q2, prev_Q3 = Q0, Q1, Q2, Q3

        # Загружаем или сдвигаем
        Q3, Qi3 = reg_bit(IN[3], 0,       prev_Q2, LOAD, SHIFT, CLK, Q3, Qi3)
        Q2, Qi2 = reg_bit(IN[2], prev_Q3, prev_Q1, LOAD, SHIFT, CLK, Q2, Qi2)
        Q1, Qi1 = reg_bit(IN[1], prev_Q2, prev_Q0, LOAD, SHIFT, CLK, Q1, Qi1)
        Q0, Qi0 = reg_bit(IN[0], prev_Q1, 0,       LOAD, SHIFT, CLK, Q0, Qi0)

        if first:
            LOAD = 0
            SHIFT = 1
            first = False

        print(f"[{tick}] Q3:{Q3} Q2:{Q2} Q1:{Q1} Q0:{Q0}")
        time.sleep(1)
