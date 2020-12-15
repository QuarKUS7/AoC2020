import pytest
from collections import defaultdict

TARGET = 2020

def initialize(entry_list):
    numbers = defaultdict(list)
    for i, k in enumerate(entry_list[:-1]):
        numbers[k].append(i)
    return numbers

def run_memory_game(last_shout, count, numbers, target):

    while count != (target-1):
        numbers[last_shout].append(count)

        if len(numbers[last_shout]) == 1:
            last_shout = 0
        else:
            indexes = numbers[last_shout][-2:]
            new_shout = indexes[-1]  - indexes[-2]
            last_shout = new_shout
        count += 1
    return last_shout

def solve(entry_list, target):
    numbers = initialize(entry_list)
    count = len(entry_list) -1
    return run_memory_game(entry_list[-1], count, numbers, target)


if __name__ == '__main__':
    with open("day15.txt", "r") as f:
        entry_list =  f.read().split()
    entry_list = [int(i) for i in entry_list[0].split(',')]

    print(solve(entry_list, TARGET))

@pytest.mark.parametrize(
    "target, entry_list, output", [(2020, [0,3,6], 436)])
def test_solve(target, entry_list, output):
    assert solve(entry_list, target) == output
