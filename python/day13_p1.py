import re
import sys


cranes = []
crane = dict()
for line in sys.stdin:
    line = line.strip()

    if not line:
        cranes.append(crane)
        crane = dict()
        continue

    name, pos = line.split(':')
    pos = re.match(r" X.(\d+), Y.(\d+)", pos)
    x, y = int(pos[1]), int(pos[2])
    crane[name] = (x, y)

cranes.append(crane)

total_cost = 0
for crane in cranes:
    p_x, p_y = crane["Prize"]
    a_x, a_y = crane["Button A"]
    b_x, b_y = crane["Button B"]
    fewest_cost = float('inf')

    for nums_a in range(101):
        remains_x = p_x - a_x * nums_a
        remains_y = p_y - a_y * nums_a

        if (
            p_x - a_x * nums_a < 0 
            or p_y - a_y * nums_a < 0
        ):
            break

        if remains_x % b_x != 0 or remains_y % b_y != 0:
            continue

        nums_b_x = remains_x // b_x
        nums_b_y = remains_y // b_y
        if nums_b_x == nums_b_y and nums_b_x <= 100:
            cost = nums_a * 3 + nums_b_x
            fewest_cost = min(cost, fewest_cost)
    
    if fewest_cost < float('inf'):
        total_cost += fewest_cost

print("day13 part01 =>", total_cost)
