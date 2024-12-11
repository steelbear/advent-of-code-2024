import sys


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            new_stones.extend(
                [int(stone[:len(stone) // 2]), int(stone[len(stone) // 2:])]
            )
        else:
            new_stones.append(stone * 2024)
    return new_stones


line = sys.stdin.readline()
stones = list(map(int, line.strip().split()))

for _ in range(25):
    stones = blink(stones)

print("day11 part01 =>", len(stones))

