import re

RANGE_REGEX = r'(\d+-\d+)'
KEY_REGEX = r'(^\w+\s?\w+)'


def get_field_ranges(raw_ranges):
    field_ranges = {}
    raw_ranges = raw_ranges.split('\n')
    for r in raw_ranges:
        key = re.findall(KEY_REGEX, r)
        se = re.findall(RANGE_REGEX, r)
        values = [int(d) for i in se for d in i.split('-')]
        field_ranges[key[0]] = values
    return field_ranges

def process_tikets(raw_ticket):
    nearby_tickets = raw_ticket.split('\n')
    nearby_tickets = [ticket for ticket in nearby_tickets[1:]]
    nearby_tickets = [i.split(',') for i in nearby_tickets if i != '']
    return nearby_tickets

def is_valid(num, fields_ranges):
    for values in fields_ranges.values():
        if values[0] <= num <= values[1] or values[2] <= num <= values[3]:
            return True
    return False

if __name__ == '__main__':

    with open("day16.txt", "r") as f:
        entry_list =  f.read().split('\n\n')

    field_ranges = get_field_ranges(entry_list[0])
    nearby_tickets = process_tikets(entry_list[-1])
    my_ticket = process_tikets(entry_list[1])


    invalid = []
    for ticket in nearby_tickets:
        for num in ticket:
            num = int(num)
            if not is_valid(num, field_ranges):
                invalid.append(num)

            for values in field_ranges.values():
                if values[0] <= num <= values[1] or values[2] <= num <= values[3]:
                    break

    print(sum(invalid))
