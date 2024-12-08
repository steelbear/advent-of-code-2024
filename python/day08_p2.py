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


antennas = dict()

for y, line in enumerate(sys.stdin):
    for x, c in enumerate(line.strip()):
        if c != '.':
            if antennas.get(c):
                antennas[c].add(Point(x, y))
            else:
                antennas[c] = set([Point(x, y)])
w, h = x + 1, y + 1 

antinodes = set()
for freq in antennas:
    nums_antennas = len(antennas[freq])
    antennas[freq] = list(antennas[freq])
    for i in range(nums_antennas - 1):
        for j in range(i + 1, nums_antennas):
            antenna_1 = antennas[freq][i]
            antenna_2 = antennas[freq][j]
            delta = antenna_1 - antenna_2

            antinodes.add(antenna_1)
            antinodes.add(antenna_2)

            antinode = antenna_1 + delta
            while is_valid(antinode, w, h):
                antinodes.add(antinode)
                antinode = antinode + delta

            antinode = antenna_2 - delta
            while is_valid(antinode, w, h):
                antinodes.add(antinode)
                antinode = antinode - delta

print("day08 part02 =>", len(antinodes))