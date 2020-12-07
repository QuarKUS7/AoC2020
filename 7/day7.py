import re
import pytest

MY_BAG = 'shiny gold'
BAG_REGEX = r'\s?\d?(.*?) bag\w?'


def parse_bags(entry_list):
    bags = {}
    for entry in entry_list:
        entry = entry.strip().replace(',','')
        bag_name, inner_bags = entry.split('contain')

        inner_bags = re.findall(BAG_REGEX, inner_bags)
        inner_bags = [inner_bag.strip() for inner_bag in inner_bags]

        inner_bags_counts = re.findall('\d+', entry)
        inner_bags_counts = [int(bag_count) for bag_count in inner_bags_counts]

        bag_name = re.findall(BAG_REGEX, bag_name)
        bags[bag_name[0]] = {bag:count for bag, count in zip(inner_bags, inner_bags_counts)}

    return bags

def can_place_shiny_gold(bag_name, bags):
    bag_content = bags[bag_name]
    if 'no other' in bag_content:
        return False
    if 'shiny gold' in bag_content:
        return True
    return any([can_place_shiny_gold(inner_bag, bags) for inner_bag in bag_content])

def solve(entry_list):
    all_bags = parse_bags(entry_list)
    positive_bags = 0
    for bag_name in all_bags.keys():
        if can_place_shiny_gold(bag_name, all_bags):
            positive_bags += 1
    return positive_bags


if __name__ == '__main__':

    with open("day7.txt", "r") as f:
        entry_list =  f.read().splitlines()

    print(solve(entry_list))

@pytest.mark.parametrize("entry_list, output", [(['light red bags contain 1 bright white bag, 2 muted yellow bags.', 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.', 'bright white bags contain 1 shiny gold bag.', 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.', 'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.', 'dark olive bags contain 3 faded blue bags, 4 dotted black bags.', 'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.', 'faded blue bags contain no other bags.', 'dotted black bags contain no other bags.'], 4)])
def test_solve(entry_list, output):
    assert solve(entry_list) == output
