import fileinput
import re
from copy import deepcopy

lines = [x.strip() for x in fileinput.input()]

start_state = []
for line in lines:
    start_state.append([x for x in line])

space = {}
for z in range(-50, 50):
    space.setdefault(z, {})
    for y in range(-50, 50):
        space[z].setdefault(y, {})
        for x in range(-50, 50):
            space[z][y][x] = '.'

for y in range(len(start_state)):
    for x in range(len(start_state[y])):
        space.setdefault(0, {})
        space[0].setdefault(y, {})
        space[0][y][x] = start_state[y][x]


def print_space(space):
    for z in space:
        print(f'z={z}')
        cur = []

        for y in space[z].values():
            cur.append(''.join([v for v in y.values()]))
        print('\n'.join(cur), end='')
    print()


def get_neighbours(x, y, z, space):
    sum = 0

    for zv in range(-1, 2):
        for yv in range(-1, 2):
            for xv in range(-1, 2):
                if not (xv == 0 and yv == 0 and zv == 0):
                    try:
                        # if space[(z + zv)%len(space)][(y + yv)%len(space[z])][(x + xv)%len(space[z][y])] == '#':
                        if space[z + zv][y + yv][x + xv] == '#':
                            sum += 1
                    except:
                        continue

    return sum


def new_state(x, y, z, state, space):
    sum = get_neighbours(x, y, z, space)

    if state == '#' and not (sum == 2 or sum == 3):
        return 'inactive'
    elif state == '.' and sum == 3:
        return 'active'

    if state == '#':
        return 'active'
    else:
        return 'inactive'


# def num_active_planes(space):
#     for z in space:
#         for y in space[z]:
#             for x in space[z][y]:
#                 if space[z][y][x] == '#':
#                     active += 1
#                     break

for i in range(6):
    # active_planes = num_active_planes(space)
    prev_space = deepcopy(space)
    for z in prev_space:
        for y in prev_space[z]:
            for x in prev_space[z][y]:
                new = new_state(x, y, z, prev_space[z][y][x], prev_space)
                if new == 'active':
                    space[z][y][x] = '#'
                elif new == 'inactive':
                    space[z][y][x] = '.'
    print(i)

sum = 0
for z in space:
    for y in space[z]:
        for x in space[z][y]:
            if space[z][y][x] == '#':
                sum += 1

print(sum)
