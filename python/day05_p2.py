import sys


def get_valid_center(nums, prohibits):
    prohibit = set()
    center = nums[len(nums) // 2]
    _nums = nums.copy()
    _nums.reverse()
    while _nums:
        num = _nums.pop()
        if num in prohibit:
            #print(nums, "- invalid")
            return -1
        if prohibits.get(num):
            prohibit = prohibit | prohibits[num]
    #print(nums, "- valid")
    return center


def find_valid_center(nums, prohibits):
    all_nums = set(nums)

    stack = [([num], prohibits[num].copy() | set([num])) for num in nums]
    while stack:
        orders, prohibit = stack.pop()
        
        if len(orders) == len(nums):
            return orders[len(orders) // 2]
        
        candidates = all_nums - prohibit
        for candidate in candidates:
            
            stack.append((orders + [candidate],
                          prohibit | set([candidate]) | prohibits[candidate])
                          )
    return None


prohibits = dict()
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    a, b = list(map(int, line.split('|')))
    if not prohibits.get(a):
        prohibits[a] = set()
    if prohibits.get(b):
        prohibits[b].add(a)
    else:
        prohibits[b] = set([a])

#print(prohibits)

result = 0
for line in sys.stdin:
    orders = list(map(int, line.strip().split(',')))
    center = get_valid_center(orders, prohibits)
    if center < 0:
        result += find_valid_center(orders, prohibits)
    #print("result:", result)

print("day05 part01 =>", result)