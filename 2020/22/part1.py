from os import sys

p1, p2 = sys.stdin.read().split('\n\n')
p1 = list(map(int, p1.split('\n')[1:]))
p2 = list(map(int, p2.split('\n')[1:]))

while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)

    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

score = 0
for i, c in enumerate(p2):
    score += (len(p2) - i) * c

print(score)
