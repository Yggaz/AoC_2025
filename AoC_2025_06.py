from math import prod
f_in = open('input_06.txt', 'r', encoding='utf-8')
sheet = f_in.readlines()
f_in.close()
rows = len(sheet)
cols = len(sheet[rows-2])
problems = len(sheet[0].split())
data = []
data2 = []
result = []
result2 = []
for r, lin in enumerate(sheet):
    if r < rows - 1:
        data.append(list(map(int, lin.strip().split())))
    else:
        oper = list(lin.strip().split())
p = 0
data2.append([])
for c in range(cols):
    n = ''
    for r in range(rows - 1):
        if c <= len(sheet[r]) - 1:
            n += sheet[r][c]
    if n.strip() == '':
        p += 1
        data2.append([])
    else:
        data2[p].append(int(n))
data1 = [[data[i][j] for i in range(rows - 1)] for j in range(problems)]
res1 = 0
res2 = 0
for p in range(problems):
    if oper[p] == '+':
        res1 += sum(data1[p])
        res2 += sum(data2[p])
    else:
        res1 += prod(data1[p])
        res2 += prod(data2[p])
print('Part 1 answer: ', res1)
print('Part 2 answer: ', res2)
