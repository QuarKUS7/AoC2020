import pytest
from day3 import count_trees


def solve(entry_list, slopes):
    total_trees = 1
    for right, down in slopes:
        slope_trees = count_trees(entry_list, down, right)
        total_trees *= slope_trees
    return total_trees


if __name__ == '__main__':
    with open("day3.txt", "r") as f:
        entry_list =  f.read().splitlines()

    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

    print(solve(entry_list, slopes))


@pytest.mark.parametrize("entry_list, slopes, output", [(['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#'], ((1,1), (3,1), (5,1), (7,1), (1,2)), 336)])
def test_solve(entry_list, slopes, output):
    assert solve(entry_list, slopes) == output
