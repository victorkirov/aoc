(values := [sum([int(i) for i in v.strip().split('\n')]) for v in open('input').read().split('\n\n')]).sort(reverse=True)
print('Part1:', max(values))
print('Part2:', sum(values[:3]))
