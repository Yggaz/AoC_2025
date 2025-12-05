res1 = 0
fresh = set()
all_fresh = []
products = False
for f in open('input_05.txt', 'r'):
    text = f.strip()
    if len(text) == 0:
        products = True
    else:
        if products:
            product = int(text)
            good = False
            for fd in fresh:
                if product <= fd[1] and product >= fd[0]:
                    good = True
            res1 += 1 if good else 0
        else:
            cur = list(map(int, text.split('-')))
            fresh.add(tuple(map(int, text.split('-'))))
            i = 0
            found = False
            while i < len(all_fresh) and not found:
                if (all_fresh[i][0] < cur[1]) and (all_fresh[i][0] > cur[0]):
                    found = True
                    all_fresh[i][0] = cur[0]
                if (all_fresh[i][1] < cur[1]) and (all_fresh[i][1] > cur[0]):
                    found = True
                    all_fresh[i][1] = cur[1]
                i += 1 if not found else 0
            if not found:
                all_fresh.append(cur)
i = 0
while i < len(all_fresh) - 1:
    found1 = False
    found2 = False
    j = i + 1
    while j < len(all_fresh):
        # левый край данного - внутри проверяемого
        if (all_fresh[i][0] >= all_fresh[j][0]) and (all_fresh[i][0] <= all_fresh[j][1]):
            found1 = True
            found2 = True
            # сдвигаем левый край данного
            all_fresh[i][0] = all_fresh[j][0]
        # правый край данного - внутри проверяемого
        if (all_fresh[i][1] >= all_fresh[j][0]) and (all_fresh[i][1] <= all_fresh[j][1]):
            found1 = True
            found2 = True
            # сдвигаем правый край данного
            all_fresh[i][1] = all_fresh[j][1]
        # проверяемый полностью внутри данного
        if (all_fresh[i][0] <= all_fresh[j][0]) and (all_fresh[i][1] >= all_fresh[j][1]):
            found1 = True
            found2 = True
        if found1:
            del all_fresh[j]
            found1 = False
        else:
            j += 1
    i += 0 if found2 else 1
print('Part 1 answer: ', res1)
res2 = sum(x[1] - x[0] + 1 for x in all_fresh)
print('Part 2 answer: ', res2)
#print(all_fresh)
