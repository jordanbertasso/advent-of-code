ins = []
with open('input.txt', 'r') as f:
    ins = f.readlines()

def terminates(replace_idx: int, replacement: str):
    i = 0
    acc = 0
    visited = []
    while i < len(ins):
        cmd, arg = ins[i].split(' ')

        if i == replace_idx:
            cmd = replacement
    
        if i in visited:
            return False, acc
    
        visited.append(i)
    
        if cmd == 'acc':
            acc += int(arg)
            i += 1
        elif cmd == 'jmp':
            i += int(arg)
        else:
            i+=1
    
    return True, acc


i = 0
acc = 0
visited = []
while i < len(ins):
    cmd = ins[i][:3]

    if cmd == 'nop':
        win, acc = terminates(i, 'jmp')
        if win:
            print(acc)
            break
    elif cmd == 'jmp':
        win, acc = terminates(i, 'nop')
        if win:
            print(acc)
            break

    i += 1
