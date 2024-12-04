import sys


def is_valid(x, y, w, h):
    return (0 <= x < w) and (0 <= y < h)


def contains_mat(needle: str, haystack: list[str], 
                 start: list[int, int],
                 dr: tuple[int, int], dc: tuple[int, int],
                 #found: list[list[bool]],
                 ):
    w, h = len(haystack[0]), len(haystack)
    len_needle = len(needle)

    count = 0
    while True:
        x, y = start
        start[0] += dc[0]
        start[1] += dc[1]

        if not is_valid(x, y, w, h):
            break
        
        matched = 0
        while is_valid(x, y, w, h):
            if mat[y][x] == needle[matched]:
                matched += 1
            elif mat[y][x] == needle[0]:
                matched = 1
            else:
                matched = 0
            if matched == len_needle:
                #_x, _y = x, y
                #for _ in range(4):
                #    found[_y][_x] = True
                #    _x -= dr[0]
                #    _y -= dr[1]
                count += 1
                matched = 0
            x += dr[0]
            y += dr[1]
    
    return count


mat = []
#found = []
for line in sys.stdin:
    mat.append(line.strip())
    #found.append([False] * len(mat[0]))

w, h = len(mat[0]), len(mat)

search_strategies = [
    ((1, 0), (0, 1), (0, 0)), # left -> right
    ((-1, 0), (0, 1), (w - 1, 0)), # right -> left
    ((0, 1), (1, 0), (0, 0)), # top -> bottom
    ((0, -1), (1, 0), (0, h - 1)), # bottom -> top
    ((1, 1), (-1, 0), (w - 1, 0)), # top left -> bottom right
    ((1, 1), (0, 1), (0, 1)),
    ((-1, -1), (0, 1), (w - 1, 0)), # bottom right -> top left
    ((-1, -1), (-1, 0), (w - 2, h - 1)),
    ((1, -1), (0, 1), (0, 0)), # bottom left -> top right
    ((1, -1), (1, 0), (1, h - 1)),
    ((-1, 1), (1, 0), (0, 0)), # top right -> bottom left
    ((-1, 1), (0, 1), (w - 1, 1)),
    ]

count = 0
for dr, dc, start in search_strategies:
    count += contains_mat("XMAS", mat, list(start), dr, dc,
                          #found
                          )

print("day04 part01 =>", count)
#for y in range(h):
#    for x in range(w):
#        if found[y][x]:
#            print(mat[y][x], end="")
#        else:
#            print('.', end="")
#    print()