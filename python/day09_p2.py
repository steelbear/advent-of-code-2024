import sys


def merge_block_near(free_blocks, fill_start, fill_size):
    master_free_i = None
    for free_i, (slave_start, slave_size) in enumerate(free_blocks):
        if (slave_start + slave_size) == fill_start:
            free_blocks[free_i] = (slave_start, slave_size + fill_size)
            master_free_i = free_i
    
    if master_free_i is None:
        master_free_i = 0
        free_blocks.insert(0, (fill_start, fill_size))

    master_start, master_size = free_blocks[master_free_i]
    
    if master_free_i < len(free_blocks) - 1:
        slave_start, slave_size = free_blocks[master_free_i + 1]
        if (master_start + master_size) == slave_start:
            free_blocks.pop(master_free_i + 1)
            free_blocks[master_free_i] = (master_start, master_size + slave_size)


fill_blocks = []
free_blocks = []

for line in sys.stdin:
    line = line.strip()
    start = 0
    for i, c in enumerate(line):
        size = int(c)
        if i % 2 == 0:
            fill_blocks.append((start, size))
        else:
            free_blocks.append((start, size))
        start += size
    break


for fill_i in range(len(fill_blocks) - 1, 0, -1):
    fill_start, fill_size = fill_blocks[fill_i]
    for free_i, (free_start, free_size) in enumerate(free_blocks):
        if fill_start < free_start:
            break

        if free_size > fill_size:
            remains_size = free_size - fill_size
            free_blocks[free_i] = (free_start + fill_size, remains_size)
            fill_blocks[fill_i] = (free_start, fill_size)
            break
        elif free_size == fill_size:
            fill_blocks[fill_i] = (free_start, fill_size)
            free_blocks.pop(free_i)
            break

checksum = 0
for fill_i, (fill_start, fill_size) in enumerate(fill_blocks):
    for i in range(fill_start, fill_start + fill_size):
        checksum += i * fill_i

print("day09 part01 =>", checksum)