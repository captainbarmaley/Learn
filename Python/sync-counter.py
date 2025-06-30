# D-Trigger on SR-LATCH
def update_d_latch(D, E, Q, Qi):
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

def t_trigger(T, CLK, Q, Qi):
    def XOR(a, b): return (a ^ b)
    D = XOR(T, Q)
    return update_d_latch(D, CLK, Q, Qi)

import time

Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1

CLK = 0
tick = 0
first_pulse = True

while True:
    CLK = 1 - CLK

    if CLK == 1:
        if first_pulse:
            first_pulse = False
        else:
            tick+=1
            value = (Q2 << 2) | (Q1 << 1) | Q0
            print(f"[{tick}] BIN: {Q2}{Q1}{Q0} | DEC: {value}")

            Q0, Qi0 = t_trigger(1, CLK, Q0, Qi0) # Переключается всегда
            Q1, Qi1 = t_trigger(1, (CLK & Qi0), Q1, Qi1) # только если Q0 = 1
            Q2, Qi2 = t_trigger(1, (CLK & Qi0 & Qi1), Q2, Qi2) # только если Q0 = 1 и Q1 = 1

    time.sleep(1)
