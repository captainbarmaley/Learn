# Choose your cat:

s = 1 # SEX: 1 - Male, 0 - Female
c = 1 # Castrated / Sterilized  
b = 1 # Black
w = 0 # White
r = 0 # Red

print(c & (s & (w | r) | (1 - s) & (1 - w) | b))
