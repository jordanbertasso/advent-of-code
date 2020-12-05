import itertools

with open('../input.txt', 'r') as f:
    report_entries = list(map(int, f.read().split('\n')[:-2]))

for one, two, three in itertools.product(report_entries, repeat=3):
    if one + two + three == 2020:
        print(one * two * three)
        break
