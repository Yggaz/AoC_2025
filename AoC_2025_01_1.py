cur = 50
zeros = 0
clicks = 0
for i, lin in enumerate(open('input_01.txt', 'r', encoding='utf-8')):
    prev = cur
    move = int(lin[1:])
    while move > 99:
        move -= 100
        clicks +=1
    if lin[0] == 'L':
        cur = cur - move
    else:
        cur = cur + move
    if cur == 0:
        zeros += 1
        clicks += 1
    elif cur < 0:
        cur += 100
        if  prev > 0:
            clicks += 1
        if cur == 0:
            zeros += 1
    elif cur > 99:
        cur -= 100
        clicks += 1
        if cur == 0:
            zeros += 1
print('Part 1 answer:', zeros)
print('Part 2 answer:', clicks)


