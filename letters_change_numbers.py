import string

text_data = input().split()

letter_digit_result = []

for text in text_data:
    letters = []
    num = ""
    for symbol in text:
        if symbol.isalpha():
            letters.append(symbol)
        else:
            num += symbol

    if letters[1].isupper():

        if letters[0].isupper():
            result = (int(num) / (string.ascii_uppercase.index(letters[0]) + 1)) - \
                     (string.ascii_uppercase.index(letters[1]) + 1)
            letter_digit_result.append(result)
        elif letters[0].islower():
            result = (int(num) * (string.ascii_lowercase.index(letters[0]) + 1)) - \
                     (string.ascii_uppercase.index(letters[1]) + 1)
            letter_digit_result.append(result)
    elif letters[1].islower():

        if letters[0].isupper():
            result = (int(num) / (string.ascii_uppercase.index(letters[0]) + 1)) + \
                     (string.ascii_lowercase.index(letters[1]) + 1)
            letter_digit_result.append(result)
        elif letters[0].islower():
            result = (int(num) * (string.ascii_lowercase.index(letters[0]) + 1)) + \
                     (string.ascii_lowercase.index(letters[1]) + 1)
            letter_digit_result.append(result)

final_result = sum(letter_digit_result)
print(f"{final_result:.2f}")
