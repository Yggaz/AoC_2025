import heapq
connections = 1000
boxes = []
distances = []
groups = []

for lin in open('input_08.txt', 'r', encoding='utf-8'):
    boxes.append(tuple(map(int, lin.split(','))))

for i in range(len(boxes) - 1):
    for j in range(i+1, len(boxes)):
        heapq.heappush(distances, ((boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2, i, j))

c = 0
while len(groups) == 0 or len(groups[0]) < len(boxes):
    dist, a, b = heapq.heappop(distances)
    c += 1
    found =-1
    k = 0
    while k < len(groups):
        if (a in groups[k]) or (b in groups[k]):
            if found < 0:
                found = k
                k += 1
            else:
                groups[found].update(groups[k])
                del groups[k]
            groups[found].add(a)
            groups[found].add(b)
        else:
            k += 1
    if found < 0:
        groups.append({a, b})
    if c == connections:
        groups.sort(key=lambda x: len(x), reverse=True)
        res1 = len(groups[0])*len(groups[1])*len(groups[2])
        print('Part 1 answer: ', res1)
res2 = boxes[a][0] * boxes[b][0]
print('Part 2 answer: ', res2)
