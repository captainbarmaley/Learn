#FULL ADDER
def full_adder(a, b, carry_in):
    sum = (a ^ b) ^ carry_in
    carry_out = (a & b) | (carry_in & (a ^ b))
    return sum, carry_out

def add_4bit(a, b):
    result = 0 # here result of operation
    carry = 0

    for i in range(4): # 4bit: 0, 1, 2, 3
        # Get 'i'bit from 'a' and 'b'
        a_bit = (a >> i) & 1
        b_bit = (b >> i) & 1

        sum_bit, carry = full_adder(a_bit, b_bit, carry)

        # Put sum_bit in 'i' position of 'result'
        result |= (sum_bit << i)
    
    result |= (carry << 4) # add newline in 5bit
    return result, carry

a = 0b1010 #10
b = 0b0111 # 7

result, carry_out = add_4bit(a, b)
print(f"{a} + {b} = {result} (carry out: {carry_out})")
print(f"Binary: {a:04b} + {b:04b} = {result:04b}")
