# IN
A = 0b1010 # 10
B = 0b0111 # 7
C_in = 0 # Carry-in bit

# 1-bit full-adder
def full_adder(A, B, C_in):
    SUM = (A ^ B) ^ C_in # Sum of bits
    C_out = (A & B) | (C_in & (A ^ B)) # Carry-out bit

    return SUM, C_out 

def decoder2to4(S1, S0):
    def AND(a, b): return a & b
    def NOT(a): return 1 - a

    Y0 = AND(NOT(S1), NOT(S0))
    Y1 = AND(NOT(S1),     S0)
    Y2 = AND(    S1,  NOT(S0))
    Y3 = AND(    S1,      S0)

    return Y0, Y1, Y2, Y3

def add_4bit(A, B, C_in):
    result = 0
    C_out = 0

    for i in range(4):
        a_bit = (A >> i) & 1
        b_bit = (B >> i) & 1

        SUM, C_out = full_adder(a_bit, b_bit, C_in)
        
        C_in = C_out
        result |= (SUM << i)

    return result, C_out

def invert(x):
    result = 0
    for i in range(4):
        x_bit = (x >> i) & 1

        i_x_bit = 1 - x_bit
        result |= (i_x_bit << i)
    return result + 1

A = int(input("Input 4bit number (1010): "))
B = int(input("Input 4bit number (0111): "))
C_in = int(input("Input carry-in bit (1 or 0): "))
choose = input("Choose operation (00 = +, 01 = -, 10 = AND, 11 = OR): ")
S1, S0 = map(int, choose)

Y0, Y1, Y2, Y3 = decoder2to4(S1, S0)

if Y0:
    result, C_out = add_4bit(A, B, C_in)
    print(f"{A} + {B} = DEC:{result} | BIN:{result:04b} | Carry-out:{C_out}")
if Y1:
    result, C_out = add_4bit(A, invert(B), C_in)
    print(f"{A} - {B} = DEC:{result} | BIN:{result:04b} | Carry-out:{C_out}")
if Y2:
    result = A & B
    print(f"{A} {'and' if result else 'not and'} {B}")
if Y3:
    result = A | B
    print(f"{A} {'or' if result else 'not or'} {B}")






