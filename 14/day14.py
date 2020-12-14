import pytest
import re

def process_input(entry_list):
    instructions = []
    for entry in entry_list:
        if 'mask' in entry:
            mask = '0b' + entry.split(' ')[-1]
            instructions.append(('mask', mask))
            continue
        items = entry.split(' ')
        value = int(items[-1])
        memory_place = re.findall(r'\d+', items[0])
        instructions.append((memory_place[0], value))
    return instructions


def save_to_memory(instructions, memory):
    for place, value in instructions:
        if place == 'mask':
            mask = value
            continue
        bin_instruction = format(value, '#038b')

        new_bin = ''
        for m, i in zip(str(mask), str(bin_instruction)):
            if m == 'X':
                new_bin += i
            else:
                new_bin += m
        memory[place] = int(new_bin, 2)
    return memory

def solve(entry_list):
    instructions = process_input(entry_list)
    memory = save_to_memory(instructions, {})
    return sum(memory.values())

if __name__ == '__main__':
    with open('day14.txt') as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))

@pytest.mark.parametrize('entry_list, output', [(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'], 165)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
