rows = []
with open('input.txt', 'r') as f:
    rows = list(map(str.strip, f.readlines()))

pos = [0, 0]

trees = 0
while pos[0] < len(rows) - 1:
    pos[1] %= len(rows[0])

    if rows[pos[0]][pos[1]] == '#':
        trees += 1

    pos[0] += 1
    pos[1] += 3

print(trees)
