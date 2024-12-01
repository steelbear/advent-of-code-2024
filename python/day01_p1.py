import sys


left_group = []
right_group = []
distance = 0

for line in sys.stdin:
    left, right = map(int, line.strip().split('   '))
    left_group.append(left)
    right_group.append(right)

left_group.sort()
right_group.sort()

for left, right in zip(left_group, right_group):
    distance += abs(left - right)

print('The distance between left and right group is', distance)