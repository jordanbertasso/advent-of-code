import fileinput
import re

exps = [l.strip() for l in fileinput.input()]


def eval(exp: str, evaled: {}):
    for prev_solved in reversed(sorted(evaled, key=len)):
        exp = exp.replace(prev_solved, str(evaled[prev_solved]))

    # Evaluate all of the addition
    while '+' in exp:
        nexp = ''
        plus_map = {}
        for m in re.finditer(r'(\d+) \+ (\d+)', exp):
            g = m.groups()
            sum = int(g[0]) + int(g[1])
            plus_map[(m.start(), m.end())] = str(sum)

        for (s, e), sum in plus_map.items():
            nexp = exp[:s] + sum + exp[e:]

        exp = nexp

    try:
        a, b = re.findall(r'(\d+)', exp)[:2]
        op = re.findall(r'(\*|\+)', exp)[0]
    except:
        return int(exp)

    sum = 0

    if op == '+':
        sum = int(a) + int(b)
    elif op == '*':
        sum = int(a) * int(b)

    l = len(a + b + op) + 3
    ops = re.findall(r'(\*|\+)', exp[l:])
    ds = re.findall(r'(\d+)', exp[l:])
    for op, d in zip(ops, ds):
        if op == '+':
            sum += int(d)
        elif op == '*':
            sum *= int(d)

    return sum


final = 0
for exp in exps:
    exp = '(' + exp + ')'

    s = []
    evaled = {}
    for i, c in enumerate(exp):
        if c == '(':
            s.append(i)
        elif c == ')':
            res = eval(exp[s[-1] + 1:i], evaled)
            evaled[exp[s[-1]:i + 1]] = res
            s.pop()

    m = max(evaled.keys(), key=len)
    final += evaled[m]

print(final)
