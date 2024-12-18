import re
import sys

WIDTH = 101
HEIGHT = 103
MID_W = WIDTH // 2
MID_H = HEIGHT // 2
QUAD_BBOXES = [
    [        0,         0, MID_W,  MID_H],
    [MID_W + 1,         0, WIDTH,  MID_H],
    [        0, MID_H + 1, MID_W, HEIGHT],
    [MID_W + 1, MID_H + 1, WIDTH, HEIGHT],
]
PATTERN = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

robots = []
for line in sys.stdin:
    matched = PATTERN.match(line)
    if matched:
        robots.append([
            int(matched[1]), 
            int(matched[2]), 
            int(matched[3]), 
            int(matched[4])
            ])
    else:
        print("Failed to match the pattern")
        sys.exit(1)

quad_factors = [0] * 4
for robot in robots:
    x, y, dx, dy = robot
    x += dx * 100
    y += dy * 100

    if x < 0:
        x += WIDTH * ((-x) // WIDTH + 1)
    if y < 0:
        y += HEIGHT * ((-y) // HEIGHT + 1)
    
    x = x % WIDTH
    y = y % HEIGHT

    for i, (from_x, from_y, to_x, to_y) in enumerate(QUAD_BBOXES):
        if from_x <= x < to_x and from_y <= y < to_y:
            quad_factors[i] += 1
            break

factor = 1
for f in quad_factors:
    factor *= f

print("day14 part1 =>", factor)