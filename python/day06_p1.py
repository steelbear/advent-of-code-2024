import sys


m = []
for line in sys.stdin:
    line = list(line.strip())
    m.append(line)

w, h = len(m[0]), len(m)

x = 0
for y in range(len(m)):
    try:
        x = m[y].index('^')
        break
    except:
        pass
m[y][x] = '.'

count = 0
i_direction = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
while True:
    dx, dy = directions[i_direction]
    next_x, next_y = x + dx, y + dy
    if 0 <= next_x < w and 0 <= next_y < h:
        if m[next_y][next_x] == '.':
            x, y = next_x, next_y
            m[y][x] = 'X'
            #print(f"({x}, {y})")
            count += 1
        elif m[next_y][next_x] == 'X':
            x, y = next_x, next_y
        else:
            i_direction = (i_direction + 1) % 4
    else:
        break

print("day06 part01 =>", count)
#for row in m:
#    print(row)