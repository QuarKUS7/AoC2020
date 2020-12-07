import pytest
from day7 import parse_bags, MY_BAG


def count_bags(bag_name, bags):
    bag_content = bags[bag_name]
    if not bag_content:
        return 0
    bag_count = sum(bag_content.values())
    return bag_count + sum([inner_bag_count * count_bags(name, bags) for name, inner_bag_count in bag_content.items()])

def solve(entry_list):
    bags = parse_bags(entry_list)

    return count_bags(MY_BAG, bags)


if __name__ == '__main__':
    with open("day7.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))


@pytest.mark.parametrize("entry_list, output", [(['shiny gold bags contain 2 dark red bags.', 'dark red bags contain 2 dark orange bags.', 'dark orange bags contain 2 dark yellow bags.', 'dark yellow bags contain 2 dark green bags.', 'dark green bags contain 2 dark blue bags.', 'dark blue bags contain 2 dark violet bags.', 'dark violet bags contain no other bags.'], 126)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
