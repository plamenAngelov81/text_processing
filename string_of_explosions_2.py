data = input()

boom = ""
i = 0
strength = 0

while i < len(data):
    letter = data[i]

    if letter == ">":
        boom += ">"
        strength += int(data[i + 1])
    else:
        if strength > 0:
            strength -= 1
        else:
            boom += letter
    i += 1

print(boom)
