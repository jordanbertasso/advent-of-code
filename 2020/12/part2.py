import fileinput

ins = [l.strip() for l in fileinput.input()]

deg = 0
N = 1
E = 10

sE = 0
sN = 0
for cmd in ins:
    print(E, N, sE, sN)
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
        oE = E
        oN = N
        if d == 90:
            E = -1 * oN
            N = oE
        elif d == 180:
            N = -1 * oN
            E = -1 * oE
        elif d == 270:
            E = oN
            N = -1 * oE
    elif cmd[0] == 'R':
        oE = E
        oN = N
        if d == 90:
            E = oN
            N = -1 * oE
        elif d == 180:
            N = -1 * oN
            E = -1 * oE
        elif d == 270:
            E = -1 * oN
            N = oE
    elif cmd[0] == 'F':
        sE += d * E
        sN += d * N

print(abs(sN) + abs(sE))
