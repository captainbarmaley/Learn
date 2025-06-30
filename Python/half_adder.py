def HALF_ADDER (a, b):
    SUM = a ^ b # XOR
    CARRY = a & b # AND
    return SUM, CARRY

print("A B | SUM CARRY")

for a in (0, 1):
    for b in (0, 1):
        s, c = HALF_ADDER(a, b)
        print(f"{a} {b} | {s}   {c}")
