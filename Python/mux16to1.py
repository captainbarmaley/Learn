# LOGIC ##################
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
#########################
# MULTIPLEX #############
def mux16to1(D, S3, S2, S1, S0):
    out_0 = mux4to1(D[0], D[1], D[2], D[3], S1, S0)
    out_1 = mux4to1(D[4], D[5], D[6], D[7], S1, S0)
    out_2 = mux4to1(D[8], D[9], D[10], D[11], S1, S0)
    out_3 = mux4to1(D[12], D[13], D[14], D[15], S1, S0)

    out = mux4to1(out_0, out_1, out_2, out_3, S3, S2)
    return out

#def mux8to1(D, S2, S1, S0):
#    out_low = mux4to1(D[0], D[1], D[2], D[3], S1, S0)
#    out_high = mux4to1(D[4], D[5], D[6], D[7], S1, S0)
#    out = mux2to1(out_low, out_high, S2)
#    return out

def mux4to1(D0, D1, D2, D3, S1, S0):
    return OR(
            AND(D0, NOT(S1), NOT(S0)),
            AND(D1, NOT(S1), S0),
            AND(D2, S1, NOT(S0)),
            AND(D3, S1, S0)
            )

def mux2to1(D0, D1, S2):
    return OR(AND(D0, NOT(S2)), AND(D1, S2))
########################

for i in range(16):
    D = [1 if j == i else 0 for j in range(16)]
    S3, S2, S1, S0 = (i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1
    print(f"S:{S3}{S2}{S1}{S0} ---> OUT:{mux16to1(D, S3, S2, S1, S0)}")
