from day5 import compute_id

FIRST_ID = 40
LAST_ID = 801


def solve(entry_list):
    my_list = [compute_id(entry) for entry in entry_list]
    original_list = range(FIRST_ID, LAST_ID+1)
    return set(my_list) ^ set(original_list)


if __name__ == "__main__":

    with open("day5.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))
