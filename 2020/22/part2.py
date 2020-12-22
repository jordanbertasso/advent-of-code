from os import sys
from collections import deque


def recursive_combat(p1, p2, game):
    rounds = set()
    while p1 and p2:
        k = (tuple(p1), tuple(p2))
        if k in rounds:
            return True

        rounds.add(k)

        c1, c2 = p1.popleft(), p2.popleft()

        if len(p1) >= c1 and len(p2) >= c2:
            new_p1 = deque([p1[x] for x in range(c1)])
            new_p2 = deque([p2[x] for x in range(c2)])
            p1wins = recursive_combat(new_p1, new_p2, game + 1)

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

    if game == 0:
        winner = p2
        if p1:
            winner = p1

        score = 0
        for i, c in enumerate(winner):
            score += (len(winner) - i) * c

        print(score)
    elif p1:
        return True
    else:
        return False


p1, p2 = sys.stdin.read().split('\n\n')
p1 = deque(map(int, p1.split('\n')[1:]))
p2 = deque(map(int, p2.split('\n')[1:]))

recursive_combat(p1, p2, 0)
