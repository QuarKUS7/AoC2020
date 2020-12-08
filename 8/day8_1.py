import copy
import pytest

from day8 import process_boot_code, GameConsole


def solve(entry_list):
    boot_code = process_boot_code(entry_list)

    for i in range(len(boot_code)):
        if boot_code[i]['operation'] == 'jmp':
            possible_boot_code = copy.deepcopy(boot_code)
            possible_boot_code[i]['operation'] = 'nop'
            device = GameConsole(possible_boot_code)
            booted_correctly = device.boot_device()
            if booted_correctly:
                return device.acculumulator

    for i in range(len(boot_code)):
        if boot_code[i]['operation'] == 'nop':
            possible_boot_code = copy.deepcopy(boot_code)
            possible_boot_code[i]['operation'] = 'jmp'
            device = GameConsole(possible_boot_code)
            device.boot_device()
            booted_correctly = device.boot_device()
            if booted_correctly:
                return device.acculumulator

if __name__ == '__main__':
    with open("day8.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'], 8)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
