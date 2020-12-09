import pytest
from itertools import combinations


def is_in_preamble(value, preamble):
    diffs = {}
    for item in preamble:
        diff = value - item
        if diff in diffs: return True
        else:
            diffs[item] = item

def solve(entry_list, preamble):
    for i in range(len(entry_list)-preamble):
        item = entry_list[i+preamble]
        preamble_vals = entry_list[i:preamble+i]
        if not is_in_preamble(item, preamble_vals):
            return item

if __name__ == '__main__':
    with open("day9.txt", "r") as f:
        entry_list =  f.read().splitlines()

    entry_list = [int(entry) for entry in entry_list]
    preamble = 25
    print(solve(entry_list, preamble))


@pytest.mark.parametrize('entry_list, target, output', [([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 5, 127)])
def test_solve(entry_list, target, output):
    assert solve(entry_list, target) == output
