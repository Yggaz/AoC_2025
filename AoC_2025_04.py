f_in = open('input_04.txt', 'r', encoding='utf-8')
maze = f_in.readlines()
f_in.close()
rolls = set()
to_be_removed = set()
res1 = 0
res2 = 0
first = True
for r,ln in enumerate(maze):
    for c in range(len(ln)):
        if ln[c] == '@':
            rolls.add((r,c))
while first or len(to_be_removed) > 0:
    to_be_removed.clear()
    for roll in rolls:
        neighbors = 1 if tuple((roll[0]-1, roll[1]-1)) in rolls else 0
        neighbors += 1 if tuple((roll[0]-1, roll[1])) in rolls else 0
        neighbors += 1 if tuple((roll[0]-1, roll[1]+1)) in rolls else 0
        neighbors += 1 if tuple((roll[0], roll[1]-1)) in rolls else 0
        neighbors += 1 if tuple((roll[0], roll[1]+1)) in rolls else 0
        neighbors += 1 if tuple((roll[0]+1, roll[1]-1)) in rolls else 0
        neighbors += 1 if tuple((roll[0]+1, roll[1])) in rolls else 0
        neighbors += 1 if tuple((roll[0]+1, roll[1]+1)) in rolls else 0
        if neighbors < 4:
            to_be_removed.add(roll)
            res1 += 1 if first else 0
    res2 += len(to_be_removed)
    rolls = rolls - to_be_removed
    first = False
print('Answer for part 1:', res1)
print('Answer for part 2:', res2)