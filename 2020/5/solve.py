passes = []
with open('input.txt', 'r') as f:
    passes = list(map(str.strip, f.readlines()))

def get_pos(s, min, max, low_char, high_char):
    if s == '':
        return max
    
    if s[0] == low_char:
        return get_pos(s[1:], min, (min+max)//2, low_char, high_char)
    elif s[0] == high_char:
        return get_pos(s[1:], (min+max)//2, max, low_char, high_char)


ids = []
for p in passes:
    row = get_pos(p[:7], 0, 127, 'F', 'B')
    col = get_pos(p[7:], 0, 7, 'L', 'R')

    id = row * 8 + col
    ids.append(id)

max = max(ids)

for valid in range(max):
    if valid not in ids:
        if valid-1 in ids and valid+1 in ids:
            print(f'{id=}')

print(f'{max=}')
