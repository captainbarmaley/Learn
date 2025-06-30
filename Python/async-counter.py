import time

# Триггер на базе D-триггера
def update_d_latch(D, E, Q, Qi):
    def NOR(a, b):
        return 1 - (a | b)
    def NOT(a):
        return 1 - a
    def AND(a, b):
        return a & b

    S = AND(D, E)
    R = AND(NOT(D), E)

    for _ in range(5):
        Q_next = NOR(R, Qi)
        Qi_next = NOR(S, Q)
        Q = Q_next
        Qi = Qi_next

    return Q, Qi

# Начальные состояния
Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1

T = 1 # Toggle всегда включен
CLK = 0
tick = 0

while True:
    CLK = 1 - CLK # Инвентируем тактовый сигнал

    # Вызовы триггеров
    next_Q0, next_Qi0 = update_d_latch(Qi0, CLK, Q0, Qi0) # DATA = Qi0, ENABLE = CLK,
    next_Q1, next_Qi1 = update_d_latch(Qi1, Q0, Q1, Qi1) # DATA = Qi1, ENABLE = Q0
    next_Q2, next_Qi2 = update_d_latch(Qi2, Q1, Q2, Qi2) # DATA = Qi2, ENABLE = Q1

    Q0, Qi0 = next_Q0, next_Qi0
    Q1, Qi1 = next_Q1, next_Qi1
    Q2, Qi2 = next_Q2, next_Qi2

    tick+=1
    print(f"[{tick}] Q2: {Q2} | Q1: {Q1} | Q0: {Q0}")
    time.sleep(1)
