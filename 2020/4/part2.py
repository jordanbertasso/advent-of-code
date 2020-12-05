import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:
    def __init__(self, raw_passport):
        groups = re.findall(r'([a-z]{3}):([\S]+)', raw_passport)

        for group in groups:
            setattr(self, group[0], group[1])

    def to_dict(self):
        return {field: getattr(self, field, "") for field in fields}

    def __repr__(self):
        return str(self.to_dict())

    def is_valid(self):
        d = self.to_dict()

        for field in fields:
            if not d.get(field, ""):
                return False

        for k, v in d.items():
            if k == 'byr':
                val = int(v)
                if val < 1920 or val > 2002:
                    return False
            elif k == 'iyr':
                val = int(v)
                if val < 2010 or val > 2020:
                    return False
            elif k == 'eyr':
                val = int(v)
                if val < 2020 or val > 2030:
                    return False
            elif k == 'hgt':
                units = v[-2:]
                try:
                    val = int(v[:-2])
                except ValueError:
                    return False

                if units != 'cm' and units != 'in':
                    return False

                if units == 'cm':
                    if val < 150 or val > 193:
                        return False
                elif units == 'in':
                    if val < 59 or val > 76:
                        return False
            elif k == 'hcl':
                hash = v[0]

                if hash != '#':
                    return False

                m = re.search(r'^#[a-f0-9]{6}$', v)
                if not m:
                    return False
            elif k == 'ecl':
                valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

                if v not in valid:
                    return False
            elif k == 'pid':
                m = re.search(r'^[0-9]{9}$', v)

                if not m:
                    return False

        return True


raw_passports = []
with open('input.txt', 'r') as f:
    raw_passports = f.read().split('\n\n')

count = 0
for raw_passport in raw_passports:
    p = Passport(raw_passport)

    if p.is_valid():
        count += 1

print(count)
