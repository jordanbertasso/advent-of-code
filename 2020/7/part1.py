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


def contains_gold(bag_type: str):
    if not bag_types[bag_type]:
        return False

    if 'shiny gold' in bag_types[bag_type].keys():
        return True

    for bag_type in bag_types[bag_type].keys():
        if contains_gold(bag_type):
            return True

    return False


valid_bags = set()
for bag_type in bag_types:
    if contains_gold(bag_type):
        valid_bags.add(bag_type)

print(len(valid_bags))
