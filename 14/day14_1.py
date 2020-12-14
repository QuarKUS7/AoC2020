import re
import itertools
import pytest

from day14 import process_input

def save_to_memory(instructions, memory):
    for place, value in instructions:
        if place == 'mask':
            mask = value
            xses = mask.count('X')
            continue

        bin_place = format(int(place), '#038b')

        new_place = ''
        for m, i in zip(str(mask), str(bin_place)):
            if m == 'X':
                new_place += m
            elif m == '0':
                new_place += i
            elif m == '1':
                new_place += str(1)
            else:
                new_place += i

        float_places = itertools.product(['0', '1'], repeat=xses)
        for replace in float_places:
            float_place = new_place
            for i in list(replace):
                float_place = float_place.replace('X', i, 1)

            memory[int(float_place, 2)] =  value
    return memory

def solve(entry_list):
    instructions = process_input(entry_list)
    memory = save_to_memory(instructions, {})
    return sum(memory.values())

if __name__ == '__main__':
    with open('day14.txt') as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))

@pytest.mark.parametrize('entry_list, output', [(['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100', 'mask = 00000000000000000000000000000000X0XX', 'mem[26] = 1'], 208)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
