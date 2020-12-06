import pytest


def process_group(entry):
    group = entry.split()
    group = [set(person) for person in group]
    return group

def count_yes_in_group(group):
    group_yes = set.union(*group)
    return len(group_yes)

def solve(entry_list):
    total_yes = 0
    for entry in entry_list:
        group = process_group(entry)
        total_yes += count_yes_in_group(group)
    return total_yes

if __name__ == '__main__':
    with open("day6.txt", "r") as f:
        entry_list =  f.read().split('\n\n')

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b\n'], 11)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
