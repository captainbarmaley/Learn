byte1 = 0b1010 # 10
byte2 = 0b0001 # 1

minusbyte2 = 0b0
carry = 0b0
result = 0b0
# byte1 - byte2 = ?

# Invert 1 to -1
for i in range(4):
    bit = (byte2 >> i) & 1
    bit = (1 - bit)
    minusbyte2 |= (bit << i)
minusbyte2 += 1

# Adder
def adder(a, b, carry_in):
    sum = (a ^ b) ^ carry_in
    carry_out = (a & b) | (carry_in & (a ^ b))
    return sum, carry_out

carry = 0

# byte 1 + minusbyte 2
for i in range(4):
    bit_a = (byte1 >> i) & 1
    bit_b = (minusbyte2 >> i) & 1

    sum, carry = adder(bit_a, bit_b, carry)

    result |= (sum << i)

print(f"{byte1:04b} - {byte2:04b} = {result:05b} | Decimal: {result} | overflow: {1 - carry}")


