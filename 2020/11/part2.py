import copy

layout = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        layout.append(list(line.strip()))


def sum_neighbours(copy, r, c):
    acc = 0
    empty = copy[r][c] == 'L'

    try:
        y = 1
        while c - y >= 0:
            if copy[r][c - y] == 'L':
                break
            elif copy[r][c - y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            y += 1
    except:
        pass

    try:
        y = 1
        while c + y < len(copy):
            if copy[r][c + y] == 'L':
                break
            elif copy[r][c + y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            y += 1
    except:
        pass

    try:
        x = 1
        while r - x >= 0:
            if copy[r - x][c] == 'L':
                break
            elif copy[r - x][c] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
    except:
        pass

    try:
        x = 1
        while r + x < len(copy):
            if copy[r + x][c] == 'L':
                break
            elif copy[r + x][c] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
    except:
        pass

    try:
        x = 1
        y = 1
        while r - x >= 0 and c - y >= 0:
            if copy[r - x][c - y] == 'L':
                break
            elif copy[r - x][c - y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
            y += 1
    except:
        pass

    try:
        x = 1
        y = 1
        while r - x >= 0 and c + y < len(copy):
            if copy[r - x][c + y] == 'L':
                break
            elif copy[r - x][c + y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
            y += 1
    except:
        pass

    try:
        x = 1
        y = 1
        while r + x < len(copy) and c - y >= 0:
            if copy[r + x][c - y] == 'L':
                break
            elif copy[r + x][c - y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
            y += 1
    except:
        pass

    try:
        x = 1
        y = 1
        while r + x < len(copy) and c + y < len(copy):
            if copy[r + x][c + y] == 'L':
                break
            elif copy[r + x][c + y] == '#':
                acc += 1
                if empty:
                    return acc
                else:
                    break
            x += 1
            y += 1
    except:
        pass

    return acc


changed = True


def becomes_occupied(copy: [], r: int, c: int):
    global changed

    if copy[r][c] == 'L' and sum_neighbours(copy, r, c) == 0:
        if changed is False:
            changed = True
        return True

    if copy[r][c] == '#' and sum_neighbours(copy, r, c) >= 5:
        if changed is False:
            changed = True
        return False
    elif copy[r][c] == '#' and sum_neighbours(copy, r, c) < 5:
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
