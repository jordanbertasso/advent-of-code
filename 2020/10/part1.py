adaps = []
with open('input.txt', 'r') as f:
    adaps = f.readlines()
    adaps = list(map(int, adaps))

adaps = sorted(adaps)
mine = max(adaps) + 3

cur_jolts = 0
diffs = {'one': 0, 'three': 0}
for adap in adaps:
    if adap - cur_jolts == 1:
        diffs['one'] = diffs['one'] + 1
    if adap - cur_jolts == 3:
        diffs['three'] = diffs['three'] + 1

    cur_jolts = adap

if mine - cur_jolts == 1:
    diffs['one'] = diffs['one'] + 1
if mine - cur_jolts == 3:
    diffs['three'] = diffs['three'] + 1

print(diffs['one'] * diffs['three'])
