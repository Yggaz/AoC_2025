# 3186651075 is too high
# 2844931734 is too high
import heapq
def intersects (seg1, seg2) -> bool:
    # seg1 и seg2 имеют перпендикулярные направления и описаны 3 числами: одно число и два числа
    # Если это вертикальная линия, то это одна абсцисса и 2 ординаты: X, Y1, Y2.
    # Если это горизонтальная линия, то это одна ордината и 2 абсциссы: Y, X1, X2.
    # Они пересекаются, если seg1.Y между seg2.Y1 и seg2.Y2, а seg2.X между seg1.X1 и seg1.X2
    # И это, разумеется, симметрично!
    return (seg2[1][0] < seg1[0] < seg2[1][1]) and (seg1[1][0] < seg2[0] < seg1[1][1])
connections = 1000
tiles = []
rectangles = []
groups = []
vertical = []
horizontal = []
for i, lin in enumerate(open('input_09.txt', 'r', encoding='utf-8')):
    tiles.append(tuple(map(int, lin.split(','))))
    if i > 0:
        if tiles[i][0] == tiles[i-1][0]:
            vertical.append((tiles[i][0],(min(tiles[i][1], tiles[i-1][1]), max(tiles[i][1], tiles[i-1][1]))))
        else:
            horizontal.append((tiles[i][1],(min(tiles[i][0], tiles[i-1][0]), max(tiles[i][0], tiles[i-1][0]))))
if tiles[i][0] == tiles[0][0]:
    vertical.append((tiles[i][0], (min(tiles[i][1], tiles[0][1]), max(tiles[i][1], tiles[0][1]))))
else:
    horizontal.append((tiles[i][1], (min(tiles[i][0], tiles[0][0]), max(tiles[i][0], tiles[0][0]))))
for i in range(len(tiles) - 1):
    for j in range(i+1, len(tiles)):
        heapq.heappush(rectangles, (-(abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1), i, j))
cnt = 0
found = False
while not found and len(rectangles) > 0:
    cnt += 1
    area, a, b = heapq.heappop(rectangles)
    x1, y1 = tiles[a]
    x2, y2 = tiles[b]
    # У нас сейчас есть 2 пары координат: абсциссы x1 и x2 и ординаты y1 и y2
    # Левый нижний угол: xmin, ymin
    # Левый верхний угол: xmin, ymax
    # Правый нижний угол: xmax, ymin
    # Правый верхний угол: xmax, ymax
    # Левая сторона: абсцисса xmin, ординаты ymin до ymax
    # Правая сторона: абсцисса xmax, ординаты ymin до ymax
    # Нижняя сторона: ордината ymin, абсциссы xmin до xmax
    # Левая сторона: ордината ymax, абсциссы xmin до xmax
    xmin, xmax, ymin, ymax = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    # Уменьшим все стороны на 1. У нужного прямоугольника теперь не должно быть пересечений со сторонами многоугольника
    left = (xmin+1, (ymin+1, ymax-1))
    right = (xmax-1, (ymin+1, ymax-1))
    down = (ymin+1, (xmin+1, xmax-1))
    up = (ymax-1, (xmin+1, xmax-1))
    if any(intersects(left, h) for h in horizontal):
        found = False
    elif any(intersects(right, h) for h in horizontal):
        found = False
    elif any(intersects(up, v) for v in vertical):
        found = False
    elif any(intersects(down, v) for v in vertical):
        found = False
    else:
        found = True
    if cnt == 1:
        res1 = -area
        print('Part 1 answer:', res1)
res2 = -area
print('Part 2 answer:', res2)
