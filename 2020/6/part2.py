groups = []
with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')
    groups = list(map(lambda x: x.split('\n'), groups))
    groups[-1].pop()

res = 0
for group in groups:
    s = {}

    for ans in group:
        for c in ans:
            cur = s.get(c, 0)
            s[c] = cur + 1
    
    for v in s.values():
        if v == len(group):
            res += 1
    
print(res)