ins = []
with open('input.txt', 'r') as f:
    ins = f.readlines()

acc = 0
i = 0
visited = []
while i < len(ins):
    cmd, arg = ins[i].split(' ')

    if i in visited:
        print(acc)
        break

    visited.append(i)

    if cmd == 'acc':
        acc += int(arg)
        i += 1
    elif cmd == 'jmp':
        i += int(arg)
    else:
        i += 1
