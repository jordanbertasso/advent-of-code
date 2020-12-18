import fileinput
import re
from copy import deepcopy

lines = [x.strip() for x in fileinput.input()]

start_state = []
for line in lines:
    start_state.append([x for x in line])

space = {}
wd = 8
zd = 10
yd = 20
xd = 20
for w in range(-wd, wd + 1):
    space[w] = {}
    for z in range(-zd, zd + 1):
        space[w][z] = {}
        for y in range(-yd, yd + 1):
            space[w][z][y] = {}
            for x in range(-xd, xd + 1):
                space[w][z][y][x] = '.'

for y in range(len(start_state)):
    for x in range(len(start_state[y])):
        space[0][0][y][x] = start_state[y][x]


def print_space(space):
    for w in space:
        for z in space[w]:
            print(f'z={z}, w={w}')
            cur = []

            for y in space[w][z].values():
                cur.append(''.join([v for v in y.values()]))
            print('\n'.join(cur), end='')
        print()


def get_neighbours(x, y, z, w, space):
    sum = 0

    for wv in range(-1, 2):
        for zv in range(-1, 2):
            for yv in range(-1, 2):
                for xv in range(-1, 2):
                    if not (wv == 0 and xv == 0 and yv == 0 and zv == 0):
                        try:
                            if space[w + wv][z + zv][y + yv][x + xv] == '#':
                                sum += 1
                        except:
                            continue

    return sum


def new_state(x, y, z, w, state, space):
    sum = get_neighbours(x, y, z, w, space)

    if state == '#' and not (sum == 2 or sum == 3):
        return 'inactive'
    elif state == '.' and sum == 3:
        return 'active'

    if state == '#':
        return 'active'
    else:
        return 'inactive'


def active_outer_dim(w, space):
    for z in space[w]:
        for y in space[w][z]:
            for x in space[w][z][y]:
                if space[w][z][y][x] == '#':
                    return True

    return False


for i in range(6):
    outer_dims_to_check = set()
    for w in space:
        if active_outer_dim(w, space):
            outer_dims_to_check |= set([w - 1, w, w + 1])

    prev_space = deepcopy(space)
    for w in prev_space:
        if w not in outer_dims_to_check:
            continue

        for z in prev_space[w]:
            for y in prev_space[w][z]:
                for x in prev_space[w][z][y]:
                    new = new_state(x, y, z, w, prev_space[w][z][y][x],
                                    prev_space)
                    if new == 'active':
                        space[w][z][y][x] = '#'
                    elif new == 'inactive':
                        space[w][z][y][x] = '.'

    print(i)

sum = 0
for w in space:
    for z in space[w]:
        for y in space[w][z]:
            for x in space[w][z][y]:
                if space[w][z][y][x] == '#':
                    sum += 1

print(sum)
