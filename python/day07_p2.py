import sys


def can_calibrate(target: int, nums: list[int]) -> bool:
    stack = [(1, nums[0], '*'), (1, nums[0], '||'), (1, nums[0], '+')] # (level, amount, next_opr)

    while stack:
        level, amount, opr = stack.pop()
        if opr == '+':
            amount += nums[level]
        elif opr == '||':
            amount = int(str(amount) + str(nums[level]))
        elif opr == '*':
            amount *= nums[level]
        
        if (level == len(nums) - 1) and amount == target:
            return True
        if (level < len(nums) - 1) and amount <= target:
            stack.append((level + 1, amount, '*'))
            stack.append((level + 1, amount, '||'))
            stack.append((level + 1, amount, '+'))

    return False


amount_calibration = 0
for line in sys.stdin:
    target, nums = line.split(':')
    target = int(target)
    nums = list(map(int, nums.strip().split()))
    if can_calibrate(target, nums):
        amount_calibration += target
    
print("day07 part02 =>", amount_calibration)