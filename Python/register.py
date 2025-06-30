def update_d_lacth_with_load(D, Load, Q, Qi):
    def NOR(a, b): return 1 - (a | b)
    def NOT(a): return 1 - a
    def AND(a, b): return a & b

    E = Load
    S = AND(D, E)
    R = AND(NOT(D), E)

    for _ in range(5):
        Q_next = NOR(R, Qi)
        Qi_next = NOR(S, Q)
        Q = Q_next
        Qi = Qi_next

    return Q, Qi

Q0, Qi0 = 0, 1
Q1, Qi1 = 0, 1
Q2, Qi2 = 0, 1
Q3, Qi3 = 0, 1

while True:
    D_input = input("Input 4-bit num (1010): ")

    if len(D_input) != 4 or any(c not in '01' for c in D_input):
        print("Error, need 4bit number")
        continue

    D3, D2, D1, D0 = map(int, D_input)
    Load = int(input("Load: "))

    Q0, Qi0 = update_d_lacth_with_load(D0, Load, Q0, Qi0)
    Q1, Qi1 = update_d_lacth_with_load(D1, Load, Q1, Qi1)
    Q2, Qi2 = update_d_lacth_with_load(D2, Load, Q2, Qi2)
    Q3, Qi3 = update_d_lacth_with_load(D3, Load, Q3, Qi3)

    print(f"REG: Q = {Q3}{Q2}{Q1}{Q0}")
    print("="*30)
