import fileinput

rows = []
with open('input.txt', 'r') as f:
    rows = [x.strip() for x in fileinput.input()]

pos = [0, 0]

trees = 0
while pos[0] < len(rows):
    pos[1] %= len(rows[0])

    if rows[pos[0]][pos[1]] == '#':
        trees += 1

    pos[0] += 1
    pos[1] += 3

print(trees)
