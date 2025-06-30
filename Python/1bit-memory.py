# 1bit memory
# Триггер - элемент памяти, который хранит 1 бит (0/1)

def NOR(a, b):
    return 1 - (a | b)

def AND(a, b):
    return a & b

def NOT(a):
    return 1 - a

# начальные состояния выходов
Q = 0
Qi = 1

while True:
    data = int(input("Data (0 or 1): "))
    enable = int(input("Enable (0=hold, 1=write): "))

    # D-Latch через SR Latch на NOR
    S = AND(data, enable)           # установка
    R = AND(NOT(data), enable)      # сброс
    
    # иммитация обратной связи. схема стабилизируется
    for _ in range(5):
        Q_next = NOR(R, Qi)
        Qi_next = NOR(Q, S)
        Q = Q_next
        Qi = Qi_next

    print(f"Data={data}, Enable={enable} → Q={Q}, ~Q={Qi}\n")

