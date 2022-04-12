def invalid_ticket(a_ticket):
    if len(a_ticket) != 20:
        return True


def match_symbol(a_ticket):
    left_part = a_ticket[0:10]
    right_part = a_ticket[10:]
    special_symbol = ""
    if 6 * '@' in left_part and 6 * '@' in right_part:
        special_symbol = '@'

    elif 6 * '#' in left_part and 6 * '#' in right_part:
        special_symbol = '#'

    elif 6 * '$' in left_part and 6 * '$' in right_part:
        special_symbol = '$'

    elif 6 * '^' in left_part and 6 * '^' in right_part:
        special_symbol = '^'

    return special_symbol


def count_num(a_symbol):
    count = 6
    for n in range(7, 11):
        if n * a_symbol in left_part and n * a_symbol in right_part:
            count += 1
    return count


tickets = [s.strip() for s in input().split(",")]
is_match = False

for ticket in tickets:
    left_part = ticket[0:10]
    right_part = ticket[10:]
    symbol = match_symbol(ticket)
    if invalid_ticket(ticket):
        print("invalid ticket")
    elif match_symbol(ticket):
        count = count_num(symbol)
        if count != 10:
            print(f'ticket "{ticket}" - {count}{symbol}')
        else:
            print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')

    else:
        print(f'ticket "{ticket}" - no match')
