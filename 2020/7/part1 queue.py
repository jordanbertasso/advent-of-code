import re
from queue import Queue

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


def get_children(bag_type: str):
    return [k for k in bag_types[bag_type]]


pos_list = []
neg_list = []
def contains_gold(bag_type: str):

    q = Queue()
    q.put(bag_type)

    while not q.empty():
        b = q.get()

        if b in pos_list:
            return True
        elif b in neg_list:
            return False

        children = get_children(b)
        for child in children:
            if child == 'shiny gold':
                pos_list.append(bag_type)
                return True
            else:
                q.put(child)
    
    neg_list.append(bag_type)
    return False

s = set()
for bag_type in bag_types:
    if contains_gold(bag_type):
        s.add(bag_type)

print(len(s))
