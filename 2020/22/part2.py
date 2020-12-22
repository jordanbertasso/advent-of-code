from os import sys


def recursive_combat(p1, p2, game):
    rounds = []
    while p1 and p2:
        if (p1.copy(), p2.copy()) in rounds:
            p2 = []
            break

        rounds.append((p1.copy(), p2.copy()))

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2:
            p1wins = recursive_combat(p1[:c1].copy(), p2[:c2].copy(), game + 1)

            if p1wins:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        elif c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    p1wins = len(p2) == 0

    if game == 0:
        winner = p2
        if p1wins:
            winner = p1

        score = 0
        for i, c in enumerate(winner):
            score += (len(winner) - i) * c

        print(score)
    else:
        return p1wins


p1, p2 = sys.stdin.read().split('\n\n')
p1 = list(map(int, p1.split('\n')[1:]))
p2 = list(map(int, p2.split('\n')[1:]))

recursive_combat(p1, p2, 0)
