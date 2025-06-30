binary = input("Input binary number: ")
oct_int = ''

while len(binary) % 3 != 0:
    binary = "0" + binary 

for i in range(0, len(binary), 3):
    num = 0
    group = binary[i:i+3]

    for j in range(len(group)):
        num += int(group[j]) * 2 ** (len(group) - j - 1)
        
    oct_int += str(num)

print(oct_int)
