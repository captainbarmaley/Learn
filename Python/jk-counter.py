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

def update_jk_trigger(J, K, Q, Qi):
    E = J | K
    if J == 0 and K == 0:
        D = Q
    elif J == 1 and K == 0:
        D = 1
    elif J == 0 and K == 1:
        D = 0
    elif J == 1 and K == 1:
        D = Qi

    return update_d_latch(D, E, Q, Qi)

def update_t_trigger(T, Q, Qi):
    if T == 1:
        J, K = Qi, Q
    else:
        J, K = 0, 0
    return update_jk_trigger(J, K, Q, Qi)

Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1

CLK = 0
ticker = 0
prev_CLK = 0

while True:
    CLK = 1 - CLK

    if prev_CLK == 0 and CLK == 1:
        Q0, Qi0 = update_t_trigger(1, Q0, Qi0)
        Q1, Qi1 = update_t_trigger(Qi0, Q1, Qi1)
        Q2, Qi2 = update_t_trigger(Qi0 & Qi1, Q2, Qi2)
        
        value = (Q2 << 2) | (Q1 << 1) | Q0 
        print(f"[{ticker}] {Q2}{Q1}{Q0} DEC: {value}")
        print("="*30)
        ticker+=1

    prev_CLK = CLK
    time.sleep(1)


