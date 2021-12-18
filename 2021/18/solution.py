from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import List

# strings
lines = [l.strip() for l in open('input') if l]
values = [eval(v) for v in lines]


def extract_definition_list(sf_number, depth=1):
    def_list = []

    [left, right] = sf_number

    if type(left) == int:
        def_list.append({
            'val': left,
            'depth': depth
        })
    else:
        def_list += extract_definition_list(left, depth + 1)

    if type(right) == int:
        def_list.append({
            'val': right,
            'depth': depth
        })
    else:
        def_list += extract_definition_list(right, depth + 1)

    return def_list


def reduce_num(num: List) -> List:
    changed = True

    while changed:
        changed = False

        # explode
        i = 0
        while i < len(num):
            entry = num[i]

            if entry['depth'] > 4:
                changed = True

                entry_l_val = entry['val']
                entry_r_val = num[i + 1]['val']
                entry_depth = entry['depth']

                num.pop(i + 1)
                entry['val'] = 0
                entry['depth'] -= 1

                if i > 0:
                    num[i - 1]['val'] += entry_l_val

                if i < len (num) - 1:
                    num[i + 1]['val'] += entry_r_val

            i += 1

        # split
        i = 0
        while i < len(num):
            entry = num[i]
            if entry['val'] > 9:
                changed = True

                entry_val = entry['val']
                entry_depth = entry['depth']
                split_entries = [
                    {
                        'val': int(entry_val / 2),
                        'depth': entry_depth + 1
                    },
                    {
                        'val': int(entry_val / 2) + entry_val % 2,
                        'depth': entry_depth + 1
                    }
                ]
                num = num[:i] + split_entries + num[i + 1:]
                break
            i += 1

    return num


def get_score(num: List):
    while len(num) > 1:
        for i in range(len(num) - 1):
            if num[i]['depth'] == num[i + 1]['depth']:
                left = num[i]
                right = num[i+1]
                num.pop(i)
                num.pop(i)

                sum_val = left['val'] * 3 + right['val'] * 2
                num = num[:i] + [{
                    'depth': left['depth'] - 1,
                    'val': sum_val
                }] + num[i:]
                break

    return num[0]['val']

# parts
def part1():
    result = extract_definition_list(values[0])

    for value in values[1:]:
        result += extract_definition_list(value)

        for val in result:
            val['depth'] += 1

        result = reduce_num(result)

    return get_score(result)

def part2():
    pass


print('Part 1: ', part1())
print('Part 2: ', part2())
