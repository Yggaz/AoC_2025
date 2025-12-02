res1 = 0
res2 = 0
with open('input_02.txt', 'r') as f:
    text = f.read().strip()
for d in text.split(','):
    bounds = d.split('-')
    b1 = int(bounds[0])
    b2 = int(bounds[1])
    for i in range(b2 - b1 + 1):
        test = b1 + i
        stest = str(test)
        if test < 10:
            continue
        good = True
        j = len(stest) // 2
        while good and (j > 0):
            if len(stest) % j == 0:
                chunks = [stest[t:t + j] for t in range(0, len(stest), j)]
                if len(set(chunks)) == 1:
                    good = False
                    res2 += test
                    if len(chunks) == 2:
                        res1 += test
            j -= 1
print('Part 1 answer: ', res1)
print('Part 2 answer: ', res2)
