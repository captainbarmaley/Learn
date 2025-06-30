def NOT(a): return 1 - a
def AND(a, b): return a & b

def decoder2to4(A1, A0):
    Y0 = AND(NOT(A1), NOT(A0))
    Y1 = AND(NOT(A1),      A0)
    Y2 = AND(A1,      NOT(A0))
    Y3 = AND(A1,           A0)

    return Y0, Y1, Y2, Y3

for A1 in [0, 1]:
    for A0 in [0, 1]:
        Y0, Y1, Y2, Y3 = decoder2to4(A1, A0)
        print(f"A1:{A1}, A0:{A0} ---> Y0:{Y0} Y1:{Y1} Y2:{Y2} Y3:{Y3}")
