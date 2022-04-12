symbols = input()

digits = ""
letters = ""
special = ""
for i in symbols:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        digits += i
    else:
        special += i

print(digits)
print(letters)
print(special)
