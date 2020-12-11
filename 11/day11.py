import copy
import pytest

TOLERANCE = 3

def switch(where, r, c):
    if where == 'down':
        return r-1, c
    elif where == 'up':
        return r+1, c
    elif where == 'right':
        return r, c+1
    elif where == 'left':
        return r, c-1
    elif where == 'leftdown':
        return r-1, c-1
    elif where == 'rightdown':
        return r-1, c+1
    elif where == 'leftup':
        return r+1, c-1
    elif where == 'rightup':
        return r+1, c+1

def count_ocoupied_from_seat(entry_list, row, column, depth, tolerance):

    positions = ['down', 'up', 'left', 'right', 'leftdown', 'rightdown', 'leftup', 'rightup']
    occupied = 0
    for position in positions:
        r = copy.deepcopy(row)
        c = copy.deepcopy(column)
        if occupied > tolerance:
            return occupied
        for _ in range(depth):
            r, c =  switch(position, r, c)
            if r < 0 or r > len(entry_list):
                break
            if c < 0 or c > len(entry_list[0]):
                break
            try:
                if entry_list[r][c] == '#':
                    occupied += 1
                    break
                elif entry_list[r][c] == 'L':
                    break
            except IndexError:
                break
    return occupied


def process_seat(entry_list, row, column, new_positions, tolerance, count_function, depth):
    place = entry_list[row][column]
    if place == 'L':
        if count_function(entry_list, row, column, depth, tolerance) == 0:
            new_positions[row][column] = '#'
    elif place == '#':
        if count_function(entry_list, row, column, depth, tolerance) > tolerance:
            new_positions[row][column] = 'L'

def run_round(entry_list, tolerance, count_function, depth):
    new_positions = copy.deepcopy(entry_list)

    for r in range(len(entry_list)):
        for c in range(len(entry_list[0])):
            process_seat(entry_list, r, c, new_positions, tolerance, count_function, depth)
    return new_positions

def solve(entry_list, tolerance, count_function, depth):

    while True:
        new_positions = run_round(entry_list, tolerance, count_function, depth)
        if new_positions == entry_list:

            break
        else:
            entry_list = new_positions

    all_occupied = [i for r in entry_list for i in r if i == '#']
    return len(all_occupied)

if __name__ == '__main__':
    with open("day11.txt", "r") as f:
        entry_list =  f.read().splitlines()

    entry_list = [list(i) for i in entry_list]

    depth = 1

    print(solve(entry_list, TOLERANCE, count_ocoupied_from_seat, depth))


@pytest.mark.parametrize('entry_list, tolerance, count_ocoupied_from_seat, depth, output', [([['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'], ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'], ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']], 3, count_ocoupied_from_seat, 1, 37)])
def test_solve(entry_list, tolerance, count_ocoupied_from_seat, depth, output):
    assert solve(entry_list, tolerance, count_ocoupied_from_seat, depth) == output

