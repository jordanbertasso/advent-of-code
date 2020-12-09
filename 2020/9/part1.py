import itertools

nums = []
with open('input.txt', 'r') as f:
    nums = f.readlines()
    nums = list(map(int, nums))


def sum_exists(target: int, start: int, end: int):
    pnums = nums[start:end]
    print(f'{pnums=}')

    for a, b in itertools.combinations(pnums, 2):
        if a + b == target:
            return True

    return False


i = 25
while i < len(nums):
    if not sum_exists(nums[i], i - 25, i):
        print(nums[i])
        break
    i += 1
