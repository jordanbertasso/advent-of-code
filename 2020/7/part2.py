import re

rules = []
with open('input.txt', 'r') as f:
    rules = f.readlines()
    rules = list(map(str.strip, rules))

bag_types = {}
for rule in rules:

    main_bag_type = rule.split(' bags')[0]
    bag_types.setdefault(main_bag_type, {})

    entries = rule.split('contain ')[1]
    entries = entries.split(',')

    for entry in entries:
        try:
            num = int(re.findall(r'(\d+)', entry)[0])
            sub_bag_type = re.findall(r'\d+ (.*) bag', entry)[0]
        except:
            continue

        bag_types[main_bag_type][sub_bag_type] = num


def get_count(bag_type: str):
    sum = 0
    for k,v in bag_types[bag_type].items():
        sum += v
        sum += v * get_count(k)
    
    return sum

print(get_count('shiny gold'))