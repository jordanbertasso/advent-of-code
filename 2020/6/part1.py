groups = []
with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')
    groups = list(map(lambda x: x.split('\n'), groups))

res = 0
for group in groups:
    s = set()

    for ans in group:
        for c in ans:
            s.add(c)

    res += len(s)

print(res)
