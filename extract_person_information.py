num = int(input())

for i in range(num):
    person_info = input()

    name_symbol_1 = "@"
    name_symbol_2 = "|"

    age_symbol_1 = "#"
    age_symbol_2 = "*"

    name_index_1 = person_info.find(name_symbol_1)
    name_index_2 = person_info.find(name_symbol_2)

    age_index_1 = person_info.find(age_symbol_1)
    age_index_2 = person_info.find(age_symbol_2)

    person_name = person_info[name_index_1 + 1: name_index_2]
    age = person_info[age_index_1 + 1: age_index_2]

    print(f"{person_name} is {age} years old.")
