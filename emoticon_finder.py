emote_string = input()

for i in range(len(emote_string)):
    if emote_string[i] == ":":
        print(emote_string[i] + emote_string[i + 1])
