from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations


p1_start = 5
p2_start = 8


# parts
def part1():
    dice = 1
    rolls = 0

    p1_pos = p1_start
    p2_pos = p2_start

    p1_score = 0
    p2_score = 0

    while 1:
        moves = 0
        for _ in range(3):
            moves += dice
            dice += 1
            rolls += 1
            if dice > 100:
                dice = 1
        p1_pos += moves
        p1_pos = ((p1_pos - 1) % 10) + 1
        p1_score += p1_pos
        if p1_score >= 1000:
            break

        moves = 0
        for _ in range(3):
            moves += dice
            dice += 1
            rolls += 1
            if dice > 100:
                dice = 1
        p2_pos += moves
        p2_pos = ((p2_pos - 1) % 10) + 1
        p2_score += p2_pos
        if p2_score >= 1000:
            break

    return min([p1_score, p2_score]) * rolls


possible_rolls = list(sum(combo) for combo in set(permutations([1,1,1,2,2,2,3,3,3], 3)))

@cache
def get_winner_counts(p1_position, p2_position, p1_score, p2_score):
    wins_1 = 0
    wins_2 = 0
    for roll in possible_rolls:
        p1_position_new = p1_position + roll
        p1_position_new = ((p1_position_new - 1) % 10) + 1
        p1_score_new = p1_score + p1_position_new

        if p1_score_new >= 21:
            wins_1 += 1
            continue
        for roll2 in possible_rolls:
            p2_position_new = p2_position + roll2
            p2_position_new = ((p2_position_new - 1) % 10) + 1
            p2_score_new = p2_score + p2_position_new

            if p2_score_new >= 21:
                wins_2 += 1
                continue

            (inner_wins_1, inner_wins_2) = get_winner_counts(
                p1_position_new,
                p2_position_new,
                p1_score_new,
                p2_score_new
            )
            wins_1 += inner_wins_1
            wins_2 += inner_wins_2

    return wins_1, wins_2


def part2():
    return max(list(get_winner_counts(p1_start, p2_start, 0, 0)))


print('Part 1: ', part1())
print('Part 2: ', part2())
