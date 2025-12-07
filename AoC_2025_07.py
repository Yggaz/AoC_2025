res1 = 0
res2 = 1
lab = []
for lin in open('input_07.txt', 'r', encoding='utf-8'):
    lab.append(lin.strip())
rows = len(lab)
cols = len(lab[0])
start = lab[0].find('S')
ways = dict()
beams = set()
beams.add(start)
ways[start] = 1
r = 1
while r < rows - 1:
    next_beams = set()
    next_ways = dict()
    for b in beams:
        if lab[r][b] == '^':
            next_ways[b - 1] = next_ways.get(b-1, 0) + ways.get(b, 0)
            next_beams.add(b-1)
            next_ways[b + 1] = next_ways.get(b+1, 0) + ways.get(b, 0)
            next_beams.add(b+1)
            res1 += 1
        else:
            next_beams.add(b)
            next_ways[b] = next_ways.get(b, 0) + ways.get(b, 0)
    beams = next_beams
    ways = next_ways
    r += 1
print('Part 1 answer: ', res1)
res2 = sum(ways[x] for x in ways.keys())
print('Part 2 answer: ', res2)
