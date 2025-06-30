def NOK(a, b):
    return (a * b) // NOD(a, b)

def NOD(a, b):
    while b:
        a, b = b, a % b
    return a

print("Calculate NOK & NOD")
a = int(input("Input 'a' number: "))
b = int(input("Input 'b' number: "))

print(f"NOD: {NOD(a, b)}")
print(f"NOK: {NOK(a, b)}")
