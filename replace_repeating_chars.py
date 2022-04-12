bugged_string = input()

letter = None

for bug in bugged_string:
    if bug != letter:
        print(bug, end="")
        letter = bug
