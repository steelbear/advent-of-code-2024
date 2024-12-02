import sys


def is_safe(nums):
    direction = nums[1] - nums[0]
    if direction == 0:
        return False
    direction = 1 if direction > 0 else -1

    for i in range(len(nums) - 1):
        diff = direction * (nums[i + 1] - nums[i])
        if 0 >= diff or diff > 3:
            return False
    return True


total = 0
safe = 0
for line in sys.stdin:
    total += 1
    nums = list(map(int, line.split()))

    if is_safe(nums):
        safe += 1
        continue

    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i + 1:]
        if is_safe(new_nums):
            safe += 1
            break
    
    
print("day02 part01 =>", safe, '/', total)
