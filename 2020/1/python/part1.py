import itertools
from os import sys

with open('../input.txt', 'r') as f:
    report_entries = f.readlines()

for one, two in itertools.product(report_entries, repeat=2):
    try:
        one = int(one.strip())
        two = int(two.strip())
    except ValueError:
        continue

    if one + two == 2020:
        print(one * two)
        sys.exit(0)
