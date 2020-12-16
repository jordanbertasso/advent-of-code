import os
import re

input = os.sys.stdin.read()

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
        print(value)
        return True

        # if value < cond[0] or value > cond[1]:
        #     print(value)
        #     return True

    return False


bad = []
for ticket in tickets:
    fields = list(map(int, ticket.split(',')))

    for value in fields:
        if value_bad(value):
            bad.append(value)

res = 0
for b in bad:
    res += b

print(res)
