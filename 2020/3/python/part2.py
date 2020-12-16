from functools import reduce
import fileinput

rows = []
with open('input.txt', 'r') as f:
    rows = [x.strip() for x in fileinput.input()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

ans = []

for slope in slopes:
    trees = 0
    pos = [0, 0]

    while pos[0] < len(rows):
        pos[1] %= len(rows[0])

        if rows[pos[0]][pos[1]] == '#':
            trees += 1

        pos[0] += slope[1]
        pos[1] += slope[0]

    ans.append(trees)

res = reduce(lambda x, y: x * y, ans)
print(res)
