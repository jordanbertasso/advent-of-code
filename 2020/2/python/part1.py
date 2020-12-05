import re
from os import sys

with open('../input.txt', 'r') as f:
    passwords = f.readlines()

count = 0
for password in passwords:
    data = password.split(' ')

    try:
        min = int(data[0].split('-')[0])
        max = int(data[0].split('-')[1])
    except:
        continue

    letter = data[1][0]

    cur = data[2].strip()

    occur = len([m.start() for m in re.finditer(letter, cur)])


    if min <= occur <= max:
        count+=1

print(count)
