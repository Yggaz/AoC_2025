def joltage (d: int, ln) -> int:
    volts = ''
    digits = d
    s = 0
    while digits > 0:
        j = s + 1
        while j < len(ln) - (digits - 1):
            if ln[s] < ln[j]:
                s = j
            j += 1
        volts += ln[s]
        s += 1
        digits -= 1
    return int(volts)


res1 = 0
res2 = 0
for i, lin in enumerate(open('input_03.txt', 'r', encoding='utf-8')):
    res1 += joltage(2, lin.strip())
    res2 += joltage(12, lin.strip())
print('Part 1 answer:', res1)
print('Part 2 answer:', res2)

