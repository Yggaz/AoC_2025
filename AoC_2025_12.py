shapes = [7, 5, 7, 7, 6, 7]
cnt = 0
for i, lin in enumerate(open('input_12.txt', 'r', encoding='utf-8')):
    ln  = lin.strip()
    if ln.find('x') > 0:
        l = ln.split(': ')
        sizes = list(map(int, l[0].split('x')))
        target = list(map(int, l[1].split()))
        area = sizes[0]*sizes[1]
        blocks = (sizes[0] // 3) * (sizes[1] // 3)
        presents = sum(target)
        if presents <= blocks:
            cnt += 1
        else:
            t = sum(a * b for a, b in zip(shapes, target))
            if t <= area:
                print('Problem!!!')
                print(ln)
    if ln == '':
        shape_section = False
print('Part 1 answer:', cnt)
