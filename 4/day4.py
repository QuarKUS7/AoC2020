import pytest

REQUERED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def process_passport(entry):
    passport_lines = entry.split('\n')
    fields_raw = [line.split(' ') for line in passport_lines]
    # Lol - v produkcii nikdy!
    # rozbalenie vnutornych listov
    fields_raw = sum(fields_raw, [])
    fields = dict(parse_raw_field(item) for item in fields_raw)
    return fields

def parse_raw_field(item):
    key = item.split(':')[0]
    try:
        val = item.split(':')[1]
    except IndexError:
        val = None
    return key, val

def has_all_fields(fields):
    return all(x in fields for x in REQUERED_FIELDS)

def solve(entry_list):
    valid_passports = 0
    for entry in entry_list:
        fields = process_passport(entry)
        if has_all_fields(fields):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    with open("day4.txt", "r") as f:
        entry_list =  f.read().split("\n\n")

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm', 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929', 'hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm', 'hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in\n'], 2)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
