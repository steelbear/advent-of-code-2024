import sys


def contains(needle, haystack, start, direction):
    x, y = start
    
    for i in range(len(needle)):
        if haystack[y][x] != needle[i]:
            return False
        x += direction[0]
        y += direction[1]
    
    return True


mat = []
#found = []
for line in sys.stdin:
    mat.append(line.strip())
#    found.append([False] * len(mat[0]))

w, h = len(mat[0]), len(mat)
count = 0
for y in range(h - 2):
    for x in range(w - 2):
        if (
            (contains("MAS", mat, (x, y), (1, 1)) or contains("MAS", mat, (x + 2, y + 2), (-1, -1)))
            and (contains("MAS", mat, (x, y + 2), (1, -1)) or contains("MAS", mat, (x + 2, y), (-1, 1)))
            ):
 #           for dx, dy in zip(range(3), range(3)):
 #               found[y + dy][x + dx] = True
 #           for dx, dy in zip(range(3), range(2, -1, -1)):
 #               found[y + dy][x + dx] = True
            count += 1

print("day04 part02 =>", count)
#for y in range(h):
#    for x in range(w):
#        if found[y][x]:
#            print(mat[y][x], end="")
#        else:
#            print('.', end="")
#    print()