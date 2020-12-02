import pytest

from day1 import find_two_sum


with open("day1.txt", "r") as f:
    entry_list =  f.read().splitlines()
    entry_list = [int(i) for i in entry_list]


def find_three_sum(n, entry_list):
    for entry in entry_list:
        diff = n - entry
        out = find_two_sum(diff, entry_list)
        if out:
            return out * entry

if __name__ == '__main__':
    print(find_three_sum(2020, entry_list))


@pytest.mark.parametrize(
    "n, entry_list, output", [(2020, [1721, 979, 366, 299, 675, 1456], 241861950)]
)
def test_find_three_sum(n, entry_list, output):
    assert find_three_sum(n, entry_list) == output


