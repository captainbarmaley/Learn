text = input("Input text: ")
new_text = []

for char in text:
    ascii_char = ord(char)
    hex_char = hex(ascii_char)
    new_text.append(hex_char)

print(f"HEX: {', '.join(new_text)}")

hex_text = input("Input HEX: ")
hex_arr = hex_text.split(" ")
new_string = ''

for item in hex_arr: 
    n_item = int(item, 16)
    new_string += chr(n_item)

print(new_string)


print("DEC | HEX | CHAR")
for i in range(32, 127):
    print(f"{i}  | {hex(i)[2:]}  | {chr(i)}")

