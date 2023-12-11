from functools import cache
from collections import defaultdict
from typing import List, Dict
from functools import cmp_to_key

card_ord ='23456789TJQKA'
card_ord2 ='J23456789TQKA'

input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [v.split(' ') for v in lines]

@cache
def get_score(value: str, joker: bool = False):
    joker_cnt = 0

    if joker:
        for c in value:
            if c == 'J':
                joker_cnt += 1
        value = value.replace('J', '')

    cnt: Dict[str, int] = defaultdict(int)

    for c in value:
        cnt[c] += 1

    if joker_cnt == 5:
        return 7

    cnts = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    cnt[cnts[0][0]] += joker_cnt

    if 5 in cnt.values():
        return 7
    if 4 in cnt.values():
        return 6
    if 3 in cnt.values() and 2 in cnt.values():
        return 5
    if 3 in cnt.values():
        return 4
    if 2 in cnt.values() and len(cnts) == 3:
        return 3
    if 2 in cnt.values():
        return 2

    return 1

def compare(a: List[str], b: List[str]):
    a_score = get_score(a[0])
    b_score = get_score(b[0])

    if a_score != b_score:
        return a_score - b_score

    for i in range(0, 5):
        if card_ord.index(a[0][i]) != card_ord.index(b[0][i]):
            return card_ord.index(a[0][i]) - card_ord.index(b[0][i])

    raise Exception('wtf', a, b, a_score, b_score)


def compare2(a: List[str], b: List[str]):
    a_score = get_score(a[0], True)
    b_score = get_score(b[0], True)

    if a_score != b_score:
        return a_score - b_score

    for i in range(0, 5):
        if card_ord2.index(a[0][i]) != card_ord2.index(b[0][i]):
            return card_ord2.index(a[0][i]) - card_ord2.index(b[0][i])

    raise Exception('wtf', a, b, a_score, b_score)


# parts
def part1():
    result = 0

    localVals = list(values)
    localVals.sort(key=cmp_to_key(compare))

    for (i, [_, bid]) in enumerate(localVals):
        result += int(bid) * (i + 1)

    return result


def part2():
    result = 0

    localVals = list(values)
    localVals.sort(key=cmp_to_key(compare2))

    for (i, [_, bid]) in enumerate(localVals):
        result += int(bid) * (i + 1)

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
