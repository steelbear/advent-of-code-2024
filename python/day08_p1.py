import sys


class Point(object):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Point(self.a - other.a, self.b - other.b)
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.a == other.a and self.b == other.b
    
    def __hash__(self):
        return hash((self.a, self.b))


def is_valid(point: Point, w: int, h: int) -> bool:
    return 0 <= point.a < w and 0 <= point.b < h


antenas = dict()

for y, line in enumerate(sys.stdin):
    for x, c in enumerate(line.strip()):
        if c != '.':
            if antenas.get(c):
                antenas[c].add(Point(x, y))
            else:
                antenas[c] = set([Point(x, y)])
w, h = x + 1, y + 1 

antinodes = set()
for freq in antenas:
    nums_antenas = len(antenas[freq])
    antenas[freq] = list(antenas[freq])
    for i in range(nums_antenas - 1):
        for j in range(i + 1, nums_antenas):
            antena_1 = antenas[freq][i]
            antena_2 = antenas[freq][j]
            delta = antena_1 - antena_2
            if is_valid(antena_1 + delta, w, h):
                antinodes.add(antena_1 + delta)
            if is_valid(antena_2 - delta, w, h):
                antinodes.add(antena_2 - delta)

print("day08 part01 =>", len(antinodes))