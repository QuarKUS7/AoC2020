import math

def process_commands(entry_list):
    comands = []
    for vaue in entry_list:
        comands.append((vaue[0], int(vaue[1:])))
    return comands

def manhattan_distance(coords):
    return abs(abs(coords['W']) - abs(coords['E'])) + abs(abs(coords['S']) - abs(coords['N']))

def solve(commands):

    ship = {'N': 0, 'E': 0, 'S': 0, 'W':0}
    actual = 'E'
    dig = 270
    DIGS = {0: 'N', 90: 'W', 180: 'S', 270:'E'}
    for comands in commands:
        move, value = comands
        if move == 'F':
            ship[actual] += value
        elif move in ['N', 'E', 'S', 'W']:
            ship[move] += value
        elif move == 'R':
            value = value %  360
            dig = (dig - value) % 360
            actual = DIGS[dig]
        elif move == 'L':
            value = value %  360
            dig = (dig + value) % 360
            actual = DIGS[dig]
    return manhattan_distance(ship)


if __name__ == '__main__':
    with open("day12.txt", "r") as f:
        entry_list =  f.read().splitlines()

    commands = process_commands(entry_list)

    print(solve(commands))

