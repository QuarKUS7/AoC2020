import copy
import pytest

from day11 import solve, count_ocoupied_from_seat

TOLERANCE = 4

if __name__ == '__main__':
    with open("day11.txt", "r") as f:
        entry_list =  f.read().splitlines()

    entry_list = [list(i) for i in entry_list]

    # Max depth
    depth = len(entry_list)

    print(solve(entry_list, TOLERANCE, count_ocoupied_from_seat, depth))


@pytest.mark.parametrize('entry_list, tolerance, count_ocoupied_from_seat, depth, output', [([['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'], ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'], ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']], 4, count_ocoupied_from_seat,10, 26)])
def test_solve(entry_list, tolerance, count_ocoupied_from_seat, depth, output):
    assert solve(entry_list, tolerance, count_ocoupied_from_seat, depth) == output

