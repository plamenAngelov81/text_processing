symbol_1 = input()
symbol_2 = input()
word = input()

start = ord(symbol_1)
end = ord(symbol_2)

symbol_string = ""

for i in range(start + 1, end):
    symbol_string += chr(i)

find_symbols = []
for x in word:
    if x in symbol_string:
        find_symbols.append(x)

total = 0

for j in find_symbols:
    total += ord(j)

print(total)
