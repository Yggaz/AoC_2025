f_in = open('input_04.txt', 'r', encoding='utf-8')
maze = f_in.readlines()
f_in.close()
rolls = set()
res1 = 0
res2 = 0
first = True
for r,ln in enumerate(maze):
    for c in range(len(ln)):
        if ln[c] == '@':
            rolls.add((r,c))
to_be_removed = set()
while first or len(to_be_removed) > 0:
    to_be_removed.clear()
    for roll in rolls:
        neighbors = 0
        if tuple((roll[0]-1, roll[1]-1)) in rolls:
            neighbors += 1
        if tuple((roll[0]-1, roll[1])) in rolls:
            neighbors += 1
        if tuple((roll[0]-1, roll[1]+1)) in rolls:
            neighbors += 1
        if tuple((roll[0], roll[1]-1)) in rolls:
            neighbors += 1
        if tuple((roll[0], roll[1]+1)) in rolls:
            neighbors += 1
        if tuple((roll[0]+1, roll[1]-1)) in rolls:
            neighbors += 1
        if tuple((roll[0]+1, roll[1])) in rolls:
            neighbors += 1
        if tuple((roll[0]+1, roll[1]+1)) in rolls:
            neighbors += 1
        if neighbors < 4:
            to_be_removed.add(roll)
            if first:
                res1 += 1
    for roll in to_be_removed:
        res2 += 1
        rolls.remove(roll)
    first = False
print('Answer for part 1:', res1)
print('Answer for part 2:', res2)