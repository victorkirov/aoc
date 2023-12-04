from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

# parts
def part1():
    result = 0

    for value in values:
        [_, vals] = value.split(':')
        [win, cards] = vals.split(' | ')

        win_nums = set([int(c) for c in win.strip().split(' ') if c])
        card_nums = set([int(c) for c in cards.strip().split(' ') if c])

        cnt = len(win_nums.intersection(card_nums))

        if cnt > 0:
            result += 2 ** (cnt - 1)

    return result


def part2():
    result = defaultdict(lambda: 1)

    for value in values:
        [card, vals] = value.split(':')
        [win, cards] = vals.split(' | ')

        card_items = card.strip().split(' ')
        card_id = int(card_items[-1])

        win_nums = set([int(c) for c in win.strip().split(' ') if c])
        card_nums = set([int(c) for c in cards.strip().split(' ') if c])

        card_cnt = result[card_id]
        win_cnt = len(win_nums.intersection(card_nums))

        for win_itt in range(win_cnt):
            next_index = card_id + win_itt + 1
            if next_index <= len(values):
                result[next_index] = result[next_index] + card_cnt

    return sum(result.values())


print('Part 1: ', part1())
print('Part 2: ', part2())
