import pytest


#TWO POINTERS TECHNIQUE
def find_contigous_list(entry_list, target):
    slow = 0
    fast = 0
    for i in range(len(entry_list)):
        contiguous_sum = 0
        slow = i
        fast = slow
        while contiguous_sum < target:
            contiguous_sum += entry_list[fast]
            if contiguous_sum == target:
                return entry_list[slow:fast+1]
            fast += 1

def solve(entry_list, target):
    contiguous_list = find_contigous_list(entry_list, target)
    return max(contiguous_list) + min(contiguous_list)

if __name__ == '__main__':
    with open("day9.txt", "r") as f:
        entry_list =  f.read().splitlines()

    entry_list = [int(entry) for entry in entry_list]
    target = 36845998
    print(solve(entry_list, target))


@pytest.mark.parametrize('entry_list, target, output', [([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 127, 62)])
def test_solve(entry_list, target, output):
    assert solve(entry_list, target) == output
