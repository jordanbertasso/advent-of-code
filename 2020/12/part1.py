import fileinput

ins = [l.strip() for l in fileinput.input()]

deg = 0
N = 0
E = 0

for cmd in ins:
    d = int(cmd[1:])

    if cmd[0] == 'N':
        N += d
    elif cmd[0] == 'S':
        N -= d
    elif cmd[0] == 'E':
        E += d
    elif cmd[0] == 'W':
        E -= d
    elif cmd[0] == 'L':
        deg += d
        deg = deg % 360
    elif cmd[0] == 'R':
        deg -= d
        deg = deg % 360
    elif cmd[0] == 'F':
        if deg == 0:
            E += d
        elif deg == 90:
            N += d
        elif deg == 180:
            E -= d
        elif deg == 270:
            N -= d

print(abs(N) + abs(E))
