import numpy as np
import scipy.optimize
from functools import lru_cache

@lru_cache(maxsize = None)
def press(t:tuple, c:tuple, bt: tuple) -> int:
    if t == c:
        return 0
    if len(bt) == 0:
        return 10000
    res = 10000
    for i in range(len(bt)):
        nc = tuple(a * b for a, b in zip (c, bt[i]))
        nb = bt[:i] + bt[i+1:]
        res = min(res, 1 + press(t, nc, nb))
    return res


res1 = 0
res2 = 0
for i, lin in enumerate(open('input_10.txt', 'r', encoding='utf-8')):
    target_state_lin = lin.split(']')[0][1:]
    target = tuple(1 if ch == '#' else -1 for ch in target_state_lin)
    current = tuple(-1 for ch in target_state_lin)
    current2 = tuple(0 for ch in target_state_lin)
    joltage_lin = lin.strip().split('{')[1][:-1]
    joltage = tuple(map(int, joltage_lin.split(',')))
    buttons_lin = lin.strip().split()[1:-1]
    buttons_list = []
    buttons_list2 = []
    for b in buttons_lin:
        initial = list(1 for ch in target_state_lin)
        initial2 = list(current2)
        for sw in b[1:-1].split(','):
            initial[int(sw)] = -1
            initial2[int(sw)] = 1
        buttons_list.append(tuple(initial))
        buttons_list2.append(tuple(initial2))
    buttons = tuple(buttons_list)
    buttons2 = tuple(buttons_list2)
    res1 += press(target, current, buttons)
    #res2 += press2(joltage, current2, buttons2)
print('Part 1 answer:', res1)
joltagenp = np.asarray(joltage)
buttonsnp = np.asarray(buttons2)
c = np.asarray([1] * len(buttonsnp))
buttonst = buttonsnp.transpose()
opt = scipy.optimize.linprog(c, A_eq=buttonst, b_eq=joltagenp, integrality=1, method="highs")
res2 += opt.fun
if not opt.success:
    print(joltagenp)
    print(buttonst)
    print(opt)
print('Part 2 answer:', int(res2))
print(press.cache_info())
