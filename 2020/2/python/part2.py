with open('../input.txt', 'r') as f:
    passwords = f.readlines()

count = 0
for password in passwords:
    data = password.split(' ')

    try:
        idx1 = int(data[0].split('-')[0])
        idx2 = int(data[0].split('-')[1])
    except:
        continue

    letter = data[1][0]
    cur = data[2].strip()

    if cur[idx1 - 1] == letter and cur[idx2 - 1] != letter:
        count+=1
    elif cur[idx1 - 1] != letter and cur[idx2 - 1] == letter:
        count+=1

print(count)
