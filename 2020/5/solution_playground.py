lines = [l.strip() for l in open('input') if l]
values = [v.translate(str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})) for v in lines]
ids = set([int(value[:7], 2) * 8 + int(value[7:], 2) for value in values])

print('Part 1', max(ids))
print('Part 2', next(iter(set(range(min(ids), max(ids))).difference(set(ids)))))
