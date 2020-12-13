import pytest


def solve(entry_list):
    time = int(entry_list[0])
    buses = [int(i) for i in entry_list[1].split(',') if not i == 'x']

    closest = []
    for bus in buses:
        diff = bus * (time // bus) + bus
        closest.append(diff-time)

    min_time = min(closest)
    min_index = closest.index(min_time)

    return buses[min_index] * min_time

if __name__ == '__main__':
    with open("day13.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize('entry_list, output', [(['939', '7,13,x,x,59,x,31,19'], 295)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
