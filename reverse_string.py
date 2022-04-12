word = input()

while True:
    if word == "end":
        break
    result = word[::-1]
    print(f"{word} = {result}")
    word = input()
