def get_bit(n, i):
    return (n >> i) & 1

def set_bit(n, i):
    return n | (1 << i)

n = 0b1010

result = get_bit(n, 1) # Получаем последний бит после сдвига на i-бит
print(f"{n:04b} = {result:04b}")


result = set_bit(n, 0) # нумерация с конца, ставит 1 на бит под номером 'i' с конца
print(f"{n:03b} = {result:04b}")
