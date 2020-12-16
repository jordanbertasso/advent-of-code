passes = []
with open('input.txt', 'r') as f:
    passes = list(map(str.strip, f.readlines()))

b = []
for p in passes:
    x = ''

    for c in p:
        if c == 'F':
            x += '0'
        elif c == 'B':
            x += '1'
        elif c == 'L':
            x += '0'
        elif c == 'R':
            x += '1'
    
    b.append(int(x, 2))

print(max(b))

b = sorted(b)

for i in range(1, len(b)):
    if b[i-1] - b[i] == -2:
        print(b[i]-1)
