def NOT(a): return 1 - a

def AND(*args):
    result = 1
    for x in args:
        result &= x
    return result

def OR(*args):
    result = 0
    for x in args:
        result |= x
    return result

def mux4to1(D0, D1, D2, D3, S1, S0):
    return OR(
            OR(AND(D0, AND(NOT(S1), NOT(S0))), AND(D1, AND(NOT(S1), S0))), 
            OR(AND(D2, AND(S1, NOT(S0))), AND(D3, AND(S1, S0)))
            )

def mux2to1(D0, D1, S2):
    return OR(AND(D0, NOT(S2)), AND(D1, S2))

def mux8to1(D, S2, S1, S0):
    out_low = mux4to1(D[0], D[1], D[2], D[3], S1, S0)
    out_high = mux4to1(D[4], D[5], D[6], D[7], S1, S0)
    out = mux2to1(out_low, out_high, S2)
    return out


for i in range(8):
    D = [1 if j == i else 0 for j in range(8)]
    S2, S1, S0 = (i >> 2) & 1, (i >> 1) & 1, i & 1
    print(f"S:{S2}{S1}{S0} ---> OUT:{mux8to1(D, S2, S1, S0)}")

