def NOT(a): return 1 - a
def AND(a, b): return a & b
def OR(a, b): return a | b

def mux2to1(A, B, S):
    return OR(AND(A, NOT(S)), AND(B, S))

for a in [0, 1]:
    for b in [0, 1]:
        for s in [0, 1]:
            print(f"A:{a}, B:{b}, S:{s} ---> Out:{mux2to1(a, b, s)}")
