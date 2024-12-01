import sys
from collections import Counter

left_group = []
right_group = []
similarity = 0

for line in sys.stdin:
    left, right = map(int, line.strip().split('   '))
    left_group.append(left)
    right_group.append(right)

left_group = Counter(left_group)
right_group = Counter(right_group)

for id, count in left_group.items():
    similarity += id * count * right_group[id]

print('The similarity between left and right group is', similarity)