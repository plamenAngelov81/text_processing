data = input()

i = 0
strength = 0
while i < len(data):
    if data[i] == ">":
        str_explode = int(data[i + 1])
        strength += str_explode
    else:
        if strength > 0:
            data = data[: i] + data[i + 1:]
            i -= 1
            strength -= 1

    i += 1

print(data)
