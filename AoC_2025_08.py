import heapq
def dist(a:tuple , b: tuple) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

connections = 10
boxes = []
distances = []
groups = []

for lin in open('input_08.txt', 'r', encoding='utf-8'):
    boxes.append(tuple(map(int, lin.split(','))))

for i in range(len(boxes) - 1):
    for j in range(i+1, len(boxes)):
        heapq.heappush(distances, (dist(boxes[i], boxes[j]), i, j))
for c in range(connections):
    dist, a, b = heapq.heappop(distances)
    #print('To connect: box ', a, '(', boxes[a][0], ',', boxes[a][1], ',', boxes[a][2], ') - box ', b, '(', boxes[b][0], ',', boxes[b][1], ',', boxes[b][2], '); dist:', dist)
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
groups.sort(key=lambda x: len(x), reverse=True)
res1 = len(groups[0])*len(groups[1])*len(groups[2])
print('Part 1 answer: ', res1)
# Just continue!
while len(groups[0]) < len(boxes):
    dist, a, b = heapq.heappop(distances)
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
res2 = boxes[a][0] * boxes[b][0]
print('Part 2 answer: ', res2)
