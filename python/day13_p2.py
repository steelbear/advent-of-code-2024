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

    # | a_x b_x | |a| = |p_x|
    # | a_y b_y | |b|   |p_y|

    # |a| = 1/det * | b_y -b_x| |p_x|
    # |b|           |-a_y  a_x| |p_y|

    p_x += 10000000000000
    p_y += 10000000000000

    det = a_x * b_y - b_x * a_y
    if det == 0:
        print("err: can't solve with determinent")
        sys.exit(1)

    a_det = b_y * p_x - b_x * p_y
    b_det = a_x * p_y - a_y * p_x

    if a_det % det != 0 or b_det % det != 0:
        print("err: solution is not integer")
        continue
    
    nums_a = a_det // det
    nums_b = b_det // det

    cost = nums_a * 3 + nums_b
    total_cost += cost

print("day13 part01 =>", total_cost)
