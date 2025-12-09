import heapq
connections = 1000
tiles = []
rectangles = []
groups = []

for lin in open('input_09.txt', 'r', encoding='utf-8'):
    tiles.append(tuple(map(int, lin.split(','))))

for i in range(len(tiles) - 1):
    for j in range(i+1, len(tiles)):
        heapq.heappush(rectangles, (-(abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1), i, j))
res1, a, b = heapq.heappop(rectangles)
print('Part 1 answer:', -res1)
