from collections import Counter

def count_differences(entry_list):
    diffs = []
    for i in range(1,len(entry_list)):
        diff = entry_list[i] - entry_list[i-1]
        diffs.append(diff)
    diffs.append(3)
    counter = Counter(diffs)
    return counter

def solve(entry_list):
    counter = count_differences(entry_list)
    return counter[3] * counter[1]

if __name__ == '__main__':

    with open("day10.txt", "r") as f:
        entry_list =  f.read().splitlines()
    entry_list = [int(entry) for entry in entry_list]
    entry_list = [0] + sorted(entry_list, reverse=False)

    solve(entry_list)


