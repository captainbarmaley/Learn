def MAJORITY(a, b, c):
    return (a & c) | (b & c) | (a & b)

print("A B C | MAJORITY")

for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            print(f"{a} {b} {c} | {MAJORITY(a, b, c)}")
