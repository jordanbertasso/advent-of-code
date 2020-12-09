import itertools

nums = []
with open('input.txt', 'r') as f:
    nums = f.readlines()
    nums = list(map(int, nums))


def sum_exists(target: int, start: int, end: int):
    pnums = nums[start:end]

    for a, b in itertools.combinations(pnums, 2):
        if a + b == target:
            return True

    return False


def contiguous_sum(target: int):
    for i in range(len(nums)):
        acc = 0
        start = i
        while acc < target:
            acc += nums[i]

            if acc == target:
                return start, i
            i += 1


def sum_smallest(s: int, e: int):
    return min(nums[s:e]) + max(nums[s:e])


start, end = contiguous_sum(248131121)

print(sum_smallest(start, end))
