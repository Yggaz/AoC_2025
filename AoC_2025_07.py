res1 = 0
lab = []
for lin in open('input_07.txt', 'r', encoding='utf-8'):
    lab.append(lin.strip())
rows = len(lab)
ways = dict()
ways[lab[0].find('S')] = 1
for r in range(1, rows - 1):
    next_ways = dict()
    for b in ways.keys():
        if lab[r][b] == '^':
            next_ways[b - 1] = next_ways.get(b-1, 0) + ways[b]
            next_ways[b + 1] = next_ways.get(b+1, 0) + ways[b]
            res1 += 1
        else:
            next_ways[b] = next_ways.get(b, 0) + ways[b]
    ways = next_ways
print('Part 1 answer: ', res1)
res2 = sum(ways[x] for x in ways.keys())
print('Part 2 answer: ', res2)
