def SUM(a, b): # Сумма двух битов, 1 ^ 0 = 1
    return a ^ b

def CARRY(a, b): # Бит переноса, 1 & 1 = 1
    return a & b

def HALF_ADDER(a, b): # Полусумматор, возвращает сумму битов и перенос бита
    return SUM(a, b), CARRY(a, b)

def FULL_ADDER(a, b, carr_in): # Полный сумматор, сначало бит 'а' и бит 'б' попадают в полусумматор
    carry_out1 = CARRY(a, b) # Оттуда сумму 2 битов мы ложим в другой полусумматор вместе с входным битом переноса
    sum_ab = SUM(a, b)
    sum_bit_out, carry_out2 = HALF_ADDER(carr_in, sum_ab) # Получаем сумму 
    carry_out = carry_out1 ^ carry_out2 # Получаем два бита переноса, суммируем их 

    return f"SUM: {sum_bit_out} | CARRY_OUT: {carry_out}"

for a in range(0, 2):
    for b in range(0, 2):
        for carry_in in range(0, 2):
            print(f"{a} + {b} + CARRY IN: {carry_in}")
            print(f"{FULL_ADDER(a, b, carry_in)}\n")
