import pytest

TREE = "#"


def count_trees(entry_list, down, right):
    width = len(entry_list[1])
    position = right
    trees = 0
    for i in range(down, len(entry_list), down):
        if entry_list[i][position] == TREE:
            trees += 1
        position += right
        position = position % width
    return trees

def solve(entry_list, down, right):
    return count_trees(entry_list, down, right)


if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        entry_list =  f.read().splitlines()

    down = 1
    right = 3

    print(solve(entry_list, down, right))


@pytest.mark.parametrize("entry_list, down, right, output", [(['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#'], 1, 3, 7)])
def test_solve(entry_list, down, right, output):
    assert solve(entry_list, down, right) == output

