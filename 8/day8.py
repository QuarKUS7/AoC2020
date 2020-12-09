import pytest


class AlreadyVisitError(Exception):
    pass

def process_boot_code(entry_list):
    boot_code = []
    for entry in entry_list:
        parsed = entry.split(' ')
        instruction = {}
        instruction['operation'] = parsed[0]
        instruction['argument'] = int(parsed[1])
        instruction['visited'] = False
        boot_code.append(instruction)
    return boot_code

class GameConsole:
    def __init__(self, boot_code):
        self.accumulator = 0
        self.pointer = 0
        self.boot_code = boot_code
        self.operations = {'acc':self.acc, 'jmp':self.jmp, 'nop':self.nop}

    def acc(self, instruction):
        self.accumulator += instruction['argument']

    def jmp(self, instruction):
        self.pointer += instruction['argument'] -1

    def nop(self, instruction):
        pass

    def get_instruction(self):
        instruction = self.boot_code[self.pointer]
        if instruction['visited']:
            raise AlreadyVisitError

        self.pointer += 1
        return instruction

    def process_instruction(self, instruction):
        operation = self.operations[instruction['operation']]
        operation(instruction)
        instruction['visited'] = True

    def boot_device(self):
        while True:
            try:
                instruction = self.get_instruction()
            except IndexError:
                return True
            except AlreadyVisitError:
                return False

            self.process_instruction(instruction)


def solve(entry_list):
    boot_code = process_boot_code(entry_list)

    device = GameConsole(boot_code)
    device.boot_device()
    return device.accumulator

if __name__ == '__main__':
    with open("day8.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'],5)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
