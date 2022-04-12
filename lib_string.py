import string
letter = ["A", "B"]
num = "2"
result = int(num) / (string.ascii_uppercase.index(letter[0]) + 1)
print(result)
