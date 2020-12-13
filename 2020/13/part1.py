import fileinput

input = [l.strip() for l in fileinput.input()]

depart_time = int(input[0])

b = input[1].split(',')
buses = []
for x in b:
    if x == 'x':
        continue
    else:
        buses.append(int(x))

times = {}
for b in buses:
    times[b] = [b * i for i in range(1, 100000)]

min = 100000000
bus = 0
for bus_id in times:
    for time in times[bus_id]:
        if time > depart_time and abs(time - depart_time) < min:
            min = abs(time - depart_time)
            bus = bus_id

print(min * bus)
