user_names = input().split(", ")

pass_condition = False
for user in user_names:
    pass_condition = False
    if 3 <= len(user) <= 16:
        pass_condition = True

        for i in user:
            if i.isalpha() or i.isdigit() or i == "-" or i == "_":
                pass_condition = True
            else:
                pass_condition = False
                break

    if pass_condition:
        print(user)
