from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

import operator

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

player_1 = [int(v) for v in values[0][1:]]
player_2 = [int(v) for v in values[1][1:]]


# parts
def part1():
    p1_cards = player_1[:]
    p2_cards = player_2[:]

    while p1_cards and p2_cards:
        p1_top = p1_cards.pop(0)
        p2_top = p2_cards.pop(0)

        if p1_top > p2_top:
            p1_cards.append(p1_top)
            p1_cards.append(p2_top)
        else:
            p2_cards.append(p2_top)
            p2_cards.append(p1_top)

    win_deck = p1_cards or p2_cards

    return sum(map(operator.mul, reversed(win_deck), range(1, len(win_deck) + 1)))


def play_round(p1_cards, p2_cards):
    p1_perms = set()
    p2_perms = set()
    winner = None

    while p1_cards and p2_cards:
        p1_hash = ''.join(map(str, p1_cards))
        p2_hash = ''.join(map(str, p2_cards))

        if p1_hash in p1_perms or p2_hash in p2_perms:
            return '1', p1_cards, p2_cards

        p1_perms.add(p1_hash)
        p2_perms.add(p2_hash)

        p1_top = p1_cards.pop(0)
        p2_top = p2_cards.pop(0)

        if p1_top <= len(p1_cards) and p2_top <= len(p2_cards):
            winner, _, _ = play_round(p1_cards[:p1_top], p2_cards[:p2_top])
        elif p1_top > p2_top:
            winner = '1'
        else:
            winner = '2'

        if winner == '1':
            p1_cards.append(p1_top)
            p1_cards.append(p2_top)
        elif winner == '2':
            p2_cards.append(p2_top)
            p2_cards.append(p1_top)
        else:
            raise RuntimeError('No')

    return winner, p1_cards, p2_cards

def part2():
    winner, p1_cards, p2_cards = play_round(player_1[:], player_2[:])

    if winner == '1':
        win_deck = p1_cards
    else:
        win_deck = p2_cards

    return sum(map(operator.mul, reversed(win_deck), range(1, len(win_deck) + 1)))


print('Part 1: ', part1())
print('Part 2: ', part2())
