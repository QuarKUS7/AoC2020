import pytest
from day15 import solve

TARGET = 30000000

if __name__ == '__main__':
    with open("day15.txt", "r") as f:
        entry_list =  f.read().split()
    entry_list = [int(i) for i in entry_list[0].split(',')]

    print(solve(entry_list, TARGET))

@pytest.mark.parametrize(
    "target, entry_list, output", [(30000000, [0,3,6], 175594)])
def test_solve(target, entry_list, output):
    assert solve(entry_list, target) == output
