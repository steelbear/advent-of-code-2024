import sys


topograph = []
starting_points = []
for y, line in enumerate(sys.stdin):
    line = line.strip()
    for x, c in enumerate(line):
        if c == '0':
            starting_points.append((x, y))
    topograph.append(list(map(int, line)))

w, h = len(topograph[0]), len(topograph)
total_trail = 0

for starting_point in starting_points:
    #print(f"Starting Point: {starting_point}")
    
    stack = [starting_point]
    visited = set()
    nums_goal = 0
    
    while stack:
        x, y = stack.pop()
        
        if topograph[y][x] == 9 and (x, y) not in visited:
            nums_goal += 1
            visited.add((x, y))
            #print(f"Find a goal: ({x}, {y})")
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (
                0 <= x + dx < w 
                and 0 <= y + dy < h
                and topograph[y][x] + 1 == topograph[y + dy][x + dx]
            ):
                stack.append((x + dx, y + dy))
    #print("Total goal:", nums_goal)
    total_trail += nums_goal

print("day10 part01 =>", total_trail)