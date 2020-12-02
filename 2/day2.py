import re
import pytest


def parse_item(item):
    clean_item = re.sub(r'\W+', ' ', item)
    return clean_item.split(' ')

def check_password(bottom, top, letter, password):
    occurence = password.count(letter)
    return int(top) >= occurence >= int(bottom)

def solve(entry_list):
    correct_passwords = 0
    for entry in entry_list:
        bottom, top, letter, password = parse_item(entry)
        if check_password(bottom, top, letter, password):
            correct_passwords+= 1

    return correct_passwords


if __name__ == '__main__':
    with open("day2.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))

@pytest.mark.parametrize("entry_list, output", [(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 2)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
