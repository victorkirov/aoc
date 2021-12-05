from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
from os import POSIX_FADV_NOREUSE

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

moves = [int(m) for m in values[0].split(',')]

number_used_map = {i: { 'used': 0, 'ind': i } for i in range(100) }

boards = []
new_board = []

for value in values[2:]:
    if not value:
        boards.append(new_board)
        new_board  = []
        continue
    new_board.append(
        [
            number_used_map[int(cell)]
            for cell
            in value.strip().replace('  ', ' ').split(' ')
        ]
    )


if new_board:
    boards.append(new_board)


# parts
def get_winning_board():
    for move in moves:
        number_used_map[move]['used'] = 1

        for board in boards:
            columns = [0] * 5
            for row in board:
                if sum([v['used'] for v in row]) == 5:
                    return board, move
                for i in range(5):
                    columns[i] += row[i]['used']

            if 5 in columns:
                return board, move


def part1():
    winning_board, winning_move = get_winning_board()
    total = sum([sum([cell['ind'] for cell in row if cell['used'] == 0]) for row in winning_board])
    return total * winning_move


for i in range(100):
    number_used_map[i]['used'] = 0


def get_losing_board():
    for move in moves:
        number_used_map[move]['used'] = 1

        boards_to_remove = []

        for board in boards:
            columns = [0] * 5
            for row in board:
                if sum([v['used'] for v in row]) == 5:
                    boards_to_remove.append(board)
                    if len(boards) == 1:
                        return boards[0], move
                for i in range(5):
                    columns[i] += row[i]['used']

            if 5 in columns:
                boards_to_remove.append(board)
                if len(boards) == 1:
                    return boards[0], move

        for board in boards_to_remove:
            try:
                boards.remove(board)
            except:
                # board that was marked to remove twice as it won in a cross
                pass


def part2():
    winning_board, winning_move = get_losing_board()
    total = sum([sum([cell['ind'] for cell in row if cell['used'] == 0]) for row in winning_board])
    return total * winning_move


print('Part 1: ', part1())
print('Part 2: ', part2())
