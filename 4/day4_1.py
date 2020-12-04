import pytest
import re

from day4 import process_passport, has_all_fields

HGT_REGEX = r'\d+'
HCL_REGEX = r'^#[0-9a-f]{5}'
PID_REGEX = r'^\d{9}$'


def validate_byr(fields):
    byr = int(fields['byr'])
    return 1920 <= byr <= 2002

def validate_iyr(fields):
    yir = int(fields['iyr'])
    return 2010 <= yir <= 2020

def validate_eyr(fields):
    eyr = int(fields['eyr'])
    return 2020 <= eyr <= 2030

def validate_hgt(fields):
    hgt = fields['hgt']
    metric = hgt[-2:]
    hgt_int = int(re.findall(HGT_REGEX, hgt)[0])
    if metric == 'cm':
        return 150 <= hgt_int <= 193
    elif metric == 'in':
        return 59 <= hgt_int <= 76

def validate_hcl(fields):
    hcl = fields['hcl']
    return re.search(HCL_REGEX, hcl)

def validate_ecl(fields):
    ecl = fields['ecl']
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(fields):
    pid = fields['pid']
    return re.search(PID_REGEX, pid)

VALIDATIONS = [validate_iyr, validate_byr, validate_eyr, validate_hgt, validate_hcl, validate_ecl, validate_pid]

def are_fields_valid(fields):
    return all(x(fields) for x in VALIDATIONS)

def solve(entry_list):
    valid_passports = 0
    for entry in entry_list:
        fields = process_passport(entry)
        if not has_all_fields(entry):
            continue
        if are_fields_valid(fields):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    with open("day4.txt", "r") as f:
        entry_list =  f.read().split("\n\n")

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926', 'iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946', 'hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277', 'hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007', 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f', 'eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm', 'hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022', 'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\n']
, 4)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
