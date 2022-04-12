rage_data = input()
rage_data = rage_data.lower()

unique_letters = []
main_rage = ""
current_rage = ""

i = 0

while i < len(rage_data):

    if not rage_data[i].isdigit():
        current_rage += rage_data[i]

        if rage_data[i] not in unique_letters:
            unique_letters.append(rage_data[i])
        i += 1

    else:
        num = ""
        while rage_data[i].isdigit():
            num += rage_data[i]
            i += 1
            if i == len(rage_data):
                break

        main_rage += current_rage.upper() * int(num)

        current_rage = ""

print(f"Unique symbols used: {len(unique_letters)}")
print(main_rage)
