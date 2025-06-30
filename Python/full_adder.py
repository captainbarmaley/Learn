def FULL_ADDER(a, b, carry_in):
    SUM = (a ^ b) ^ carry_in # (A XOR B) XOR CARRY_IN = (0 ^ 0) ^ 1 = 1 SUM
    CARRY_OUT = (a & b) | (carry_in & (a ^ b))
    # (A AND B) OR (CARRY_IN AND (A XOR B))
    # (0 AND 0) OR (1 AND (0 XOR 0))
    return SUM, CARRY_OUT

print("A B CARRY_IN | SUM CARRY_OUT")
for a in (0, 1):
    for b in (0, 1):
        for carry_in in (0, 1):
            summ, carry_out = FULL_ADDER(a, b, carry_in)
            print(f"{a} {b} {carry_in}        | {summ}   {carry_out}")
