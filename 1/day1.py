import pytest


def find_two_sum(target, entry_list):
    diffs = {}
    for entry in entry_list:
        diff = target - entry
        if diff in diffs:
            return entry * diffs[diff]
        else:
            diffs[entry] = entry

if __name__ == '__main__':

    with open("day1.txt", "r") as f:
        entry_list =  f.read().splitlines()
    entry_list = [int(i) for i in entry_list]

    print(find_two_sum(2020, entry_list))


@pytest.mark.parametrize(
    "target, entry_list, output", [(2020, [1721, 979, 366, 299, 675, 1456], 514579)])
def test_find_two_sum(target, entry_list, output):
    assert find_two_sum(target, entry_list) == output

