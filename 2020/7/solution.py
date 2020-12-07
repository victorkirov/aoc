from collections import defaultdict

# lines
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

bag_mapping = defaultdict(set)
bag_child_mapping = defaultdict(dict)

for value in values:
    value = value.replace('bags', 'bag')
    outer_bag = value[:value.index('contain')].strip()

    inner_bags_value = value[value.index('contain') + 7:].strip().strip('.')

    while ',' in inner_bags_value:
        inner_bag = inner_bags_value[:inner_bags_value.index(',')].strip()
        inner_bag_count = inner_bag[:inner_bag.index(' ')]

        inner_bag = inner_bag[inner_bag.index(' '):].strip()
        inner_bags_value = inner_bags_value[inner_bags_value.index(',') + 1:].strip()

        bag_mapping[inner_bag].add(outer_bag)

        if 'no' not in inner_bag_count:
            if inner_bag not in bag_child_mapping[outer_bag]:
                bag_child_mapping[outer_bag][inner_bag] = {}

            bag_child_mapping[outer_bag][inner_bag] = int(inner_bag_count)

    inner_bag_count = inner_bags_value[:inner_bags_value.index(' ')]
    inner_bag = inner_bags_value[inner_bags_value.index(' '):].strip()

    bag_mapping[inner_bag].add(outer_bag)

    if 'no' not in inner_bag_count:
        if inner_bag not in bag_child_mapping[outer_bag]:
            bag_child_mapping[outer_bag][inner_bag] = {}

        bag_child_mapping[outer_bag][inner_bag] = int(inner_bag_count)


def part1():
    result = set()

    bags = ['shiny gold bag']

    while len(bags) > 0:
        current = bags.pop()
        bag_parent_set = bag_mapping[current]

        for bag in bag_parent_set - result:
            bags.append(bag)

        result.update(bag_parent_set)

    return len(result)


def part2():
    bags = [('shiny gold bag', 1)]

    def get_bag_child_count(parent_bag):
        children = bag_child_mapping[parent_bag]
        child_count = 0

        for child, child_cnt in children.items():
            child_count += child_cnt * get_bag_child_count(child)

        return child_count + 1

    return get_bag_child_count('shiny gold bag') - 1


print('Part 1: ', part1())
print('Part 2: ', part2())
