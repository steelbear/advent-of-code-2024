import argparse
import os
import re
import sys
import time

WIDTH = 101
HEIGHT = 103
MID_W = WIDTH // 2
MID_H = HEIGHT // 2
PATTERN = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str, required=True)
parser.add_argument("-s", type=int, default=0)
parser.add_argument("-e", type=int, required=True)
parser.add_argument("-t", type=int, default=1)

args = parser.parse_args()


def print_screen(screen, i):
    #os.system('clear' if os.name == 'posix' else 'cls')
    print()
    for row in screen:
        for c in row:
            print('@' if c > 0 else ' ', end='')
        print()
    print('time:', i)
    #time.sleep(0.5)


screen = [[0] * WIDTH for _ in range(HEIGHT)]

robots = []
f = open(args.i, 'r')
for line in f.readlines():
    matched = PATTERN.match(line)
    if matched:
        x, y, dx, dy = (int(matched[1]), 
                        int(matched[2]), 
                        int(matched[3]), 
                        int(matched[4]))
        
        dx = dx if dx >= 0 else dx + WIDTH
        dy = dy if dy >= 0 else dy + HEIGHT

        x = (x + (dx * args.s % WIDTH)) % WIDTH
        y = (y + (dy * args.s % HEIGHT)) % HEIGHT

        screen[y][x] += 1
        
        robots.append([x, y, dx, dy])
    else:
        print("Failed to match the pattern")
        sys.exit(1)
f.close()

print_screen(screen, args.s)
for t in range(args.s + args.t, args.e, args.t):
    for robot in robots:
        x, y, dx, dy = robot
        
        screen[y][x] -= 1
        
        x = (x + (dx * args.t % WIDTH)) % WIDTH
        y = (y + (dy * args.t % HEIGHT)) % HEIGHT

        robot[0] = x
        robot[1] = y

        screen[y][x] += 1
    print_screen(screen, t)
