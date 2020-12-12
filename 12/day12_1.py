import math

from day12 import process_commands, manhattan_distance

def solve(commands):
    ship = {'N': 0, 'E': 0, 'S': 0, 'W':0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W':0}

    DIGS_INT = {0: 'N', 90: 'W', 180: 'S', 270:'E'}
    DIGS = {'N': 0, 'W': 90, 'S':180, 'E':270}

    for comands in commands:
        move, value = comands
        if move == 'F':
            for key, val in ship.items():
                ship[key] += waypoint[key]*value
        elif move in ['N', 'E', 'S', 'W']:
            waypoint[move] += value
        elif move == 'R':
            value = value %  360
            new_way = {}
            for key,val in waypoint.items():
                new_key = (DIGS[key] - value + 360) % 360
                new_way[DIGS_INT[new_key]] = val
            waypoint = new_way
        elif move == 'L':
            value = value %  360
            new_way = {}
            for key,val in waypoint.items():
                new_key =  (DIGS[key] + value + 360) % 360
                new_way[DIGS_INT[new_key]] = val
            waypoint = new_way
    return manhattan_distance(ship)


if __name__ == '__main__':
    with open("day12.txt", "r") as f:
        entry_list =  f.read().splitlines()

    commands = process_commands(entry_list)

    print(solve(commands))





