from os import sys
import re

input = sys.stdin.read()

s = input.split('\n\n')
rules = s[0].split('\n')
mine = s[1].split('\n')[1]
tickets = s[2].split('\n')[1:]

conds = {}
for rule in rules:
    field_name = rule.split(':')[0]

    pairs = re.findall(r'(\d+-\d+)', rule)
    for pair in pairs:
        s = pair.split('-')
        min = int(s[0])
        max = int(s[1])

        c = conds.get(field_name, [])
        if not c:
            conds[field_name] = [(min, max)]
        else:
            conds[field_name].append((min, max))


def value_bad(value: int):
    valid = []
    for cond_list in conds.values():
        for cond in cond_list:
            for x in range(cond[0], cond[1] + 1):
                valid.append(x)

    if value not in valid:
        return True

    return False


bad_vals = []
good = []
for ticket in tickets:
    bad = False
    fields = list(map(int, ticket.split(',')))

    for value in fields:
        if value_bad(value):
            bad_vals.append(value)
            bad = True

    if not bad:
        good.append(ticket)

res = 0
for b in bad_vals:
    res += b

position_values = {}
for ticket in good:
    fields = list(map(int, ticket.split(',')))

    for i, value in enumerate(fields):
        cur = position_values.get(i, [])
        if not cur:
            position_values[i] = [value]
        else:
            position_values[i].append(value)


def value_bad_for_cond(value, cond_list):
    valid = []
    for cond in cond_list:
        for x in range(cond[0], cond[1] + 1):
            valid.append(x)

    if value not in valid:
        return True

    return False


def position_matches(position: [], cond_name: str, cond_list: [()]):
    for value in position:
        if value_bad_for_cond(value, cond_list):
            return False

    return True


conds_found = {}
for cond_name, cond_list in conds.items():
    found = False

    for i, position in position_values.items():
        if i in conds_found.values():
            continue
        if found:
            break

        if position_matches(position, cond_name, cond_list):
            cur = conds_found.get(cond_name, [])
            if cur:
                conds_found[cond_name].append(i)
            else:
                conds_found[cond_name] = [i]

min_cond = ''
min_cond_val = 0
certain = {}
while len(certain) < len(conds_found):
    min = 10000
    for k, v in conds_found.items():
        if len(v) < min:
            min_cond = k
            min_cond_val = v[0]
            min = len(v)

    for k in conds_found:
        try:
            conds_found[k].remove(min_cond_val)
        except:
            continue

    certain[min_cond] = min_cond_val
    conds_found[min_cond] = [0] * 100000

res = 1
for i, field in enumerate(map(int, mine.split(','))):
    for k, v in certain.items():
        if i == v and 'departure' in k:
            res *= field

print(res)
