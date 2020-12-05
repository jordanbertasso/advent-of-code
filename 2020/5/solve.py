passes = []
with open('input.txt', 'r') as f:
    passes = list(map(str.strip, f.readlines()))

def get_row(s, min=0, max=127):
    if s == '':
        return max
    
    if s[0] == 'F':
        return get_row(s[1:], min, (min+max)//2)
    elif s[0] == 'B':
        return get_row(s[1:], (min+max)//2, max)

def get_col(s, min=0, max=7):
    if s == '':
        return max
    
    if s[0] == 'L':
        return get_col(s[1:], min, (min+max)//2)
    elif s[0] == 'R':
        return get_col(s[1:], (min+max)//2, max)


ids = []
for p in passes:
    row = get_row(p[:7])
    col = get_col(p[7:])

    id = row * 8 + col
    ids.append(id)

max = max(ids)

valids = []
for r in range(127):
    for c in range(7):
        valids.append(r * 8 + c)

for valid in valids:
    if valid not in ids:
        if valid-1 in ids and valid+1 in ids:
            print(f'{id=}')

print(f'{max=}')
