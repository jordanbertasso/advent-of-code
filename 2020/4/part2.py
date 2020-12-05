#!/Users/jbertasso/.pyenv/shims/python
import re

passports = []
with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def bad_pass(groups):
    present_fields = [x[0] for x in groups]
    for field in fields:
        if field not in present_fields:
            return True
    
    if len(present_fields) != len(fields) and len(present_fields) != len(fields)+1:
        return True

    for group in groups:
        if group[0] == 'byr':
            val = int(group[1])
            if val < 1920 or val > 2002:
                return True
        elif group[0] == 'iyr':
            val = int(group[1])
            if val < 2010 or val > 2020:
                return True
        elif group[0] == 'eyr':
            val = int(group[1])
            if val < 2020 or val > 2030:
                return True
        elif group[0] == 'hgt':
            units = group[1][-2:]
            try:
                val = int(group[1][:-2])
            except:
                return True

            if units != 'cm' and units != 'in':
                return True

            if units == 'cm':
                if val < 150 or val > 193:
                    return True
            elif units == 'in':
                if val < 59 or val > 76:
                    return True
        elif group[0] == 'hcl':
            hash = group[1][0]
            
            if hash != '#':
                return True

            m = re.search(r'^#[a-f0-9]{6}$', group[1])
            if not m:
                return True
        elif group[0] == 'ecl':
            valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            
            if group[1] not in valid:
                return True
        elif group[0] == 'pid':
            val = group[1]
            m = re.search(r'^[0-9]{9}$', val)

            if not m:
                return True
        
    return False

count = 0
for passport in passports:
    groups = re.findall(r'([a-z]{3}):([\S]+)', passport)

    if bad_pass(groups):
        continue
    else:
        count+=1

print(count)
