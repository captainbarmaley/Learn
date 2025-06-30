def NOT(a): return 1 - a
def AND(*args):
    result = 1
    for x in args:
        result &= x
    return result

# Decoder 2 to 4
def decoder2to4(A1, A0):
    return [
        AND(NOT(A1), NOT(A0)),
        AND(NOT(A1),     A0),
        AND(    A1,  NOT(A0)),
        AND(    A1,      A0),
    ]

# Decoder 4 to 16 на базе двух 2 на 4
def decoder4to16(A3, A2, A1, A0):
    enable_lines = decoder2to4(A3, A2) # 4 блока
    sub_outputs = decoder2to4(A1, A0) # 4 выхода в блоке

    Y = [0] * 16
    for i in range(4): # по блокам
        for j in range(4): # по линиям в блоке
            Y[i * 4 + j] = AND(enable_lines[i], sub_outputs[j])
    return Y

# цикл проверки
for A3 in [0, 1]:
    for A2 in [0, 1]:
        for A1 in [0, 1]:
            for A0 in [0, 1]:
                Y = decoder4to16(A3, A2, A1, A0)
                index = A3*8 + A2*4 + A1*2 + A0
                active = [i for i, y in enumerate(Y) if y == 1]
                print(f"A:{A3}{A2}{A1}{A0} ---> active: Y{active}")
    
