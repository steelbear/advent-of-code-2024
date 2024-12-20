import sys


DIRECTIONS = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1),
}


def push_boxes(x, y, dx, dy, board):
    stack = [(x + dx, y + dy)]
    while stack:
        _x, _y = stack[-1]
        if board[_y][_x] == '.':
            break
        elif board[_y][_x] == 'O':
            stack.append((_x + dx, _y + dy))
        else:
            return x, y
    
    end_x, end_y = stack[-1]
    board[y + dy][x + dx], board[end_y][end_x] = board[end_y][end_x], board[y + dy][x + dx]

    return x + dx, y + dy


board = []
robot = None
for y, line in enumerate(sys.stdin):
    line = line.strip()
    
    if not line:
        break

    board.append(list(line))
    for x, c in enumerate(line):
        if c == '@':
            board[y][x] = '.'
            robot = (x, y)
            break

w, h = len(board[0]), len(board)

x, y = robot
for line in sys.stdin:
    operations = line.strip()
    for op in operations:
        dx, dy = DIRECTIONS[op]
        _x, _y = x + dx, y + dy

        if board[_y][_x] == '.':
            x, y = _x, _y
        elif board[_y][_x] == 'O':
            x, y = push_boxes(x, y, dx, dy, board)

coordinates = 0
for y, row in enumerate(board):
    for x, c in enumerate(row):
        if c == 'O':
            coordinates += 100 * y + x

print("Day 15 part 01 =>", coordinates)
