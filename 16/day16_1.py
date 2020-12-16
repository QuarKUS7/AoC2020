import re

from day16 import RANGE_REGEX, KEY_REGEX, get_field_ranges, process_tikets, is_valid

def find_valide(tickets):
    valid = []
    for ticket in tickets:
        if all([is_valid(int(num), field_ranges) for num in ticket]):
            valid.append(ticket)
    return valid

def find_possible_field_name(nearby_tickets, field_ranges):
    possible_fields = {}

    for i, ticket in enumerate(nearby_tickets):

        possible_fields[i] = []
        for key,value in field_ranges.items():
            if all(is_valid(int(num), {key:value}) for num in ticket):
                possible_fields[i].append(key)

    return possible_fields

if __name__ == '__main__':

    with open("day16.txt", "r") as f:
        entry_list =  f.read().split('\n\n')

    field_ranges = get_field_ranges(entry_list[0])
    nearby_tickets = process_tikets(entry_list[-1])
    my_ticket = process_tikets(entry_list[1])

    nearby_tickets = find_valide(nearby_tickets)

    # Transpose
    nearby_tickets = list(map(list, zip(*nearby_tickets)))

    possible_fields = find_possible_field_name(nearby_tickets, field_ranges)

    order = {}
    while possible_fields:
        for k,v in possible_fields.items():
            if len(v)  == 1:
                order[v[0]] = k
                break
        del possible_fields[k]
        dd = v[0]
        for k,v in possible_fields.items():
            v.remove(dd)

    multiple = 1

    for k,v in order.items():
        if 'departure' in k:
            multiple *= int(my_ticket[0][v])
    print(multiple)
