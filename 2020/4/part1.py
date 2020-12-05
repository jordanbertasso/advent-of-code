#!/Users/jbertasso/.pyenv/shims/python
import re

passports = []
with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def bad_pass(passport):
    for field in fields:
        if not re.findall(field, passport):
            return True


count = 0
for passport in passports:
    if bad_pass(passport):
        continue
    else:
        count += 1

print(count)
