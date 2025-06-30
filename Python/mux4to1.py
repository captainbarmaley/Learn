def NOT(a): return 1 - a
def AND(a, b, c): return a & b & c
def OR(a, b): return a | b

def mux4to1(D0, D1, D2, D3, S1, S0):
    return AND(D0, NOT(S1), NOT(S0)) + AND(D1, NOT(S1), S0) + AND(D2, S1, NOT(S0)) + AND(D3, S1, S0)

for S1 in [0, 1]:
    for S0 in [0, 1]:
        print(f"S:{S1}{S0} ---> OUT: {mux4to1(0, 1, 1, 0, S1, S0)}")
