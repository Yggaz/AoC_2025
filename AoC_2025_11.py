def cnt(entr:str, exit:str):
    memo = {}
    def dfsv(n):
        if n == exit:
            return 1
        if n in memo.keys():
            return memo[n]
        memo[n] = sum(dfsv(nn) for nn in devices.get(n, []))
        return memo[n]
    return dfsv(entr)


devices = dict()
for i, lin in enumerate(open('input_11.txt', 'r', encoding='utf-8')):
    ln = lin.strip().split(':')
    devices[ln[0]] = tuple(ln[1].split())
res1 = cnt('you', 'out')
print('Part 1 answer:', res1)
res2 = max(cnt('svr', 'fft') * cnt('fft', 'dac') * cnt('dac', 'out'), cnt('svr', 'dac') * cnt('dac', 'fft') * cnt('fft', 'out'))
print('Part 2 answer:', res2)
