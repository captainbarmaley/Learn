#FULL ADDER
def full_adder(a, b, carry_in):
    sum = (a ^ b) ^ carry_in
    carry_out = (a & b) | (carry_in & (a ^ b))
    return sum, carry_out

def add_8bit(a, b):
    result = 0
    carry = 0


    for i in range(8):
        a_bit = (a >> i) & 1
        b_bit = (b >> i) & 1

        sum_bit, carry = full_adder(a_bit, b_bit, carry)

        result |= (sum_bit << i)
    
    result |= (carry << 8)
    return result
        
a = 0b00000001
b = 0b00100100

result = add_8bit(a, b)
print(f"{a} + {b} = {result}")
print(f"Binary: {result:08b}")
