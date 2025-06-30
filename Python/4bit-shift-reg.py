import time

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

def reg_bit(IN, LEFT, RIGHT, LOAD, SHIFT, SHIFT_DIR, CLK, Q, Qi):
    if LOAD:
        D = IN
    elif SHIFT:
        D = RIGHT if SHIFT_DIR else LEFT
    else:
        D = Q
    return update_d_latch(D, CLK, Q, Qi)

Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1
Q3, Qi3 = 0, 1

IN = [1, 0, 1, 0]

LOAD = 1
SHIFT = 0
SHIFT_DIR = 1
first = True
CLK = 0

for tick in range(10):
    CLK = 1 - CLK

    if CLK == 1:
        prev_Q0, prev_Q1, prev_Q2, prev_Q3 = Q0, Q1, Q2, Q3

        Q3, Qi3 = reg_bit(IN[3], prev_Q2, 0,       LOAD, SHIFT, SHIFT_DIR, CLK, Q3, Qi3)
        Q2, Qi2 = reg_bit(IN[2], prev_Q1, prev_Q3, LOAD, SHIFT, SHIFT_DIR, CLK, Q2, Qi2)
        Q1, Qi1 = reg_bit(IN[1], prev_Q0, prev_Q2, LOAD, SHIFT, SHIFT_DIR, CLK, Q1, Qi1)
        Q0, Qi0 = reg_bit(IN[0], 0,       prev_Q1, LOAD, SHIFT, SHIFT_DIR, CLK, Q0, Qi0)

        if first:
            LOAD = 0
            SHIFT = 1
            SHIFT_DIR = 1
            first = False

        print(f"[{tick}] Q3:{Q3} Q2:{Q2} Q1:{Q1} Q0:{Q0}")
        time.sleep(1)
