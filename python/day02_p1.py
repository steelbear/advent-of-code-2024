import sys

total = 0
unsafe = 0
for line in sys.stdin:
    total += 1
    nums = list(map(int, line.split()))

    direction = nums[1] - nums[0]
    if direction == 0:
        unsafe += 1
        continue
    direction = 1 if direction > 0 else -1

    for i in range(len(nums) - 1):
        diff = direction * (nums[i + 1] - nums[i])
        if 0 >= diff or diff > 3:
            unsafe += 1
            break
    
print("day02 part01 =>", total - unsafe, '/', total)
