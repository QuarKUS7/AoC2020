import pytest

def binary_to_decimal(entry, top, upper):
    bottom = 0
    for i in entry:
        new = (top - bottom) // 2 + 1
        if i in upper:
            top = top - new
        else:
            bottom = bottom + new
    return bottom if i == upper else top

def compute_id(entry):
    row = binary_to_decimal(entry[:7], 127, 'F')
    columns = binary_to_decimal(entry[7:], 7, 'L')
    _id = 8 * row + columns
    return _id

def solve(entry_list):
    highest = 0
    for entry in entry_list:
        _id = compute_id(entry)
        if _id > highest:
            highest = _id
    return highest

if __name__ == "__main__":

    with open("day5.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'], 820)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
