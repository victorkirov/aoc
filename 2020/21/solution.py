from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

# map
allergen_map = defaultdict(list)
recipes = []

for value in values:
    allergens = value[value.index('(contains ') + len('(contains '):-1]
    allergens = [allergen.strip() for allergen in allergens.split(',')]

    ingredients = value[:value.index('(contains ')].strip().split(' ')
    recipes.append(ingredients)

    for allergen in allergens:
        allergen_map[allergen].append(ingredients)


# parts
def part1():
    unsafe = set()

    for ingredient_lists in allergen_map.values():
        n_unsafe = None
        for ingredient_list in ingredient_lists:
            if n_unsafe is None:
                n_unsafe = set(ingredient_list)
            else:
                n_unsafe.intersection_update(ingredient_list)

        unsafe |= n_unsafe

    safe = []
    for ingredient_list in recipes:
        for item in ingredient_list:
            if item not in unsafe:
                safe.append(item)

    return safe


def part2():
    a_map = {}
    for allergen, ingredient_lists in allergen_map.items():
        a_unsafe = None
        for ingredient_list in ingredient_lists:
            if a_unsafe is None:
                a_unsafe = set(ingredient_list)
            else:
                a_unsafe.intersection_update(set(ingredient_list))
        a_map[allergen] = a_unsafe

    clear_list = [i for i, a in a_map.items() if len(a) == 1]
    while len(clear_list) != len(a_map):
        for clear_a in clear_list:
            for a in a_map:
                if clear_a == a:
                    continue
                a_map[a].difference_update(a_map[clear_a])
        clear_list = [i for i, a in a_map.items() if len(a) == 1]

    result = ''
    for k in sorted(a_map.keys()):
        result += list(a_map[k])[0]
        result += ','

    return result[:-1]


print('Part 1: ', len(part1()))
print('Part 2: ', part2())
