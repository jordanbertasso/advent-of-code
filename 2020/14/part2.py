import fileinput
import re
import itertools

lines = [l.strip() for l in fileinput.input()]

mask = ''
loc = 0
val = []
mem = {}
for l in lines:
    m = re.findall(r'(mask) = (.*)|(mem)\[(.*)\] = (.*)', l)
    m = [x for x in m[0] if x]

    if m[0] == 'mask':
        mask = m[1]
    elif m[0] == 'mem':
        loc = list(bin(int(m[1]))[2:].rjust(36, '0'))
        val = int(m[2])

        for i in range(len(loc)):
            if mask[-i - 1] == 'X':
                loc[-1 - i] = 'X'
            elif mask[-i - 1] == '0':
                continue
            elif mask[-i - 1] == '1':
                loc[-1 - i] = '1'

        xs = len([x for x in loc if x == 'X'])
        coms = list(itertools.product(['0', '1'], repeat=xs))

        loc = ''.join(loc)
        for com in coms:
            tmp = loc
            newloc = tmp.replace('X', '%s') % com
            mem[int('0b' + newloc, 2)] = val

ans = 0
for v in mem.values():
    ans += v

print(ans)
