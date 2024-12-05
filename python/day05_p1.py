import sys


def get_valid_center(nums, prohibits):
    prohibit = set()
    center = nums[len(nums) // 2]
    nums.reverse()
    while nums:
        num = nums.pop()
        if num in prohibit:
            return 0
        if prohibits.get(num):
            prohibit = prohibit | prohibits[num]
    return center


prohibits = dict()
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    a, b = list(map(int, line.split('|')))
    if prohibits.get(b):
        prohibits[b].add(a)
    else:
        prohibits[b] = set([a])

result = 0
for line in sys.stdin:
    orders = list(map(int, line.strip().split(',')))
    result += get_valid_center(orders, prohibits)

print("day05 part01 =>", result)