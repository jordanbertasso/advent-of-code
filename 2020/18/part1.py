import fileinput
import re

exps = [l.strip() for l in fileinput.input()]


def evaluate_group(exp: str, evaled: {}):
    for prev_solved in reversed(sorted(evaled, key=len)):
        exp = exp.replace(prev_solved, str(evaled[prev_solved]))

    sum = 0

    a, b = re.findall(r'(\d+)', exp)[:2]
    op = re.findall(r'(\*|\+)', exp)[0]

    if op == '+':
        sum = int(a) + int(b)
    elif op == '*':
        sum = int(a) * int(b)

    l = len(a) + len(b) + len(op) + 3
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
            res = evaluate_group(exp[s[-1] + 1:i], evaled)
            evaled[exp[s[-1]:i + 1]] = res
            s.pop()

    m = max(evaled.keys(), key=len)
    final += evaled[m]

print(final)
