import copy

layout = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        layout.append(list(line.strip()))


def sum_neighbours(copy, r, c):
    acc = 0

    try:
        if c == 0:
            pass
        elif copy[r][c - 1] == '#':
            acc += 1
    except:
        pass
    try:
        if copy[r][c + 1] == '#':
            acc += 1
    except:
        pass
    try:
        if r == 0:
            pass
        elif copy[r - 1][c] == '#':
            acc += 1
    except:
        pass
    try:
        if copy[r + 1][c] == '#':
            acc += 1
    except:
        pass
    try:
        if r == 0 or c == 0:
            pass
        elif copy[r - 1][c - 1] == '#':
            acc += 1
    except:
        pass
    try:
        if r == 0:
            pass
        elif copy[r - 1][c + 1] == '#':
            acc += 1
    except:
        pass
    try:
        if c == 0:
            pass
        elif copy[r + 1][c - 1] == '#':
            acc += 1
    except:
        pass
    try:
        if copy[r + 1][c + 1] == '#':
            acc += 1
    except:
        pass

    return acc


changed = True


def becomes_occupied(copy: [], r: int, c: int):
    global changed

    if copy[r][c] == 'L' and sum_neighbours(copy, r, c) == 0:
        if changed == False:
            changed = True
        return True

    if copy[r][c] == '#' and sum_neighbours(copy, r, c) >= 4:
        if changed == False:
            changed = True
        return False
    elif copy[r][c] == '#' and sum_neighbours(copy, r, c) < 4:
        return True

    return False


copy = []
while changed:
    copy = []
    for i in range(len(layout)):
        copy.append([])
        for j in range(len(layout[i])):
            copy[i].append(layout[i][j])

    changed = False
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            if not copy[i][j] == '.':
                if becomes_occupied(copy, i, j):
                    layout[i][j] = '#'
                else:
                    layout[i][j] = 'L'

res = 0
for i in range(len(layout)):
    for j in range(len(layout[i])):
        if layout[i][j] == '#':
            res += 1

print(res)
