oct = '35'
sum = 0
oct = oct[::-1]
count = 0

for i_oct in oct:
    i_oct = int(i_oct)

    sum += i_oct * 8 ** count
    count+=1 

print(sum)

bin = ''

for i in range(8):
    bin = bin + str(sum % 2)
    sum = int(sum / 2)
print(bin[::-1])
