words = input().split()
words = sorted(words, key=lambda el: -len(el))
total = 0
for i in range(len(words[0])):
    if i < len(words[1]):
        total += (ord(words[0][i])) * ord(words[1][i])
    else:
        total += ord(words[0][i])
print(total)
