import sys


fill_blocks = []
free_blocks = []

for line in sys.stdin:
    line = line.strip()
    for i, c in enumerate(line):
        if i % 2 == 0:
            fill_blocks.append(int(c))
        else:
            free_blocks.append(int(c))
    break

left = 0
right = len(fill_blocks) - 1
free_i = 0
i = 0
is_left = True
checksum = 0

while left <= right:
    if is_left:
        while fill_blocks[left] > 0:
            checksum += i * left
            i += 1
            fill_blocks[left] -= 1
        left += 1
    else:
        while free_blocks[free_i] > 0 and fill_blocks[right] > 0:
            checksum += i * right
            i += 1
            free_blocks[free_i] -= 1
            fill_blocks[right] -= 1
            if fill_blocks[right] == 0:
                right -= 1
        free_i += 1
    is_left = not is_left

print("day09 part01 =>", checksum)