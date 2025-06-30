from typing import Counter


dec = input("Input number: ")
i_dec = int(dec)
hexx = ''

for i in range(4):
    char = str(int(i_dec / (16 ** (3 - i))))
    if char == '10':
        char = 'A'
    elif char == '11':
        char = 'B'
    elif char == '12':
        char = 'C'
    elif char == '13':
        char = 'D'
    elif char == '14':
        char = 'E'
    elif char == '15':
        char = 'F'
    hexx += char
    i_dec = i_dec % (16 ** (3 - i))

print(hexx)

hexx = input("Input Hex num: ")
count = len(hexx) - 1
dec = 0
for char in hexx:
    if char == 'A':
        char = '10'
    elif char == 'B':
        char = '11'
    elif char == 'C':
        char = '12'
    elif char == 'D':
        char = '13'
    elif char == 'E':
        char = '14'
    elif char == 'F':
        char = '15'
    
    num = int(char) * (16 ** count)
    count -= 1
    dec += num

print(dec)
