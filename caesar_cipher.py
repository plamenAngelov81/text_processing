string_data = input()

for letter in string_data:
    print(chr(ord(letter) + 3), end="")

# print("".join([chr(ord(letter) + 3) for letter in input()]))
