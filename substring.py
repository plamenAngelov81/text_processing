string_1 = input()
string_2 = input()

while True:
    if string_1 not in string_2:
        break
    string_2 = string_2.replace(string_1, "")

print(string_2)
