import pytest
from day2 import parse_item


def real_check_password(bottom, top, letter, password):
    first = letter == password[top]
    second = letter == password[bottom]
    # XOR
    return first != second

def solve(entry_list):
    correct_passwords = 0
    for entry in entry_list:
        bottom, top, letter, password = parse_item(entry)
        if real_check_password(int(bottom)-1, int(top)-1, letter, password):
            correct_passwords+= 1
    return correct_passwords


if __name__ == '__main__':
    with open("day2.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 1)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
