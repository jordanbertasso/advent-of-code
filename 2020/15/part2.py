import fileinput

nums = list(map(int, fileinput.input().readline().split(',')))

spoken = []
mem = {}
for turn, num in enumerate(nums):
    turn = turn + 1

    if num not in mem.keys():
        mem[num] = [turn]
        spoken.append(num)

turn = 1 + len(nums)
while True:
    try:
        s = mem[spoken[-1]][-1] - mem[spoken[-1]][-2]
    except:
        s = 0

    if turn == 30000000:
        print(s)
        break
    spoken.append(s)

    try:
        mem[s].append(turn)
    except:
        mem[s] = [turn]

    turn += 1
