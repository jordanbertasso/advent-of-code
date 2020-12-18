import fileinput
import re

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
        loc = int(m[1])
        val = list(bin(int(m[2]))[2:].rjust(36, '0'))

        for i in range(len(val)):

            if mask[-i - 1] == 'x':
                continue
            elif mask[-i - 1] == '0':
                val[-1 - i] = '0'
            elif mask[-i - 1] == '1':
                val[-1 - i] = '1'

        mem[loc] = ''.join(val)

ans = 0
for v in mem.values():
    ans += int('0b' + v, 2)

print(ans)
