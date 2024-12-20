import sys
from collections import deque


DIRECTIONS = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1),
}


def debug_board(board):
    for row in board:
        for c in row:
            print(c, end='')
        print()


def push_unique_pos(x, y, collection, visited):
    if (x, y) not in visited:
        collection.append((x, y))
        visited.add((x, y))


def push_boxes(x, y, dx, dy, board):
    #print(f"push_boxes({x}, {y}, {dx}, {dy}, board)")

    stack = []
    queue = deque([(x + dx, y + dy)])

    visited_queue = set()
    visited_stack = set()

    while queue:
        _x, _y = queue.popleft()
        if board[_y][_x] == '.':
            push_unique_pos(_x, _y, stack, visited_stack)
        elif board[_y][_x] == '[':
            if dx == 0:
                push_unique_pos(_x + dx, _y + dy, queue, visited_queue)
                push_unique_pos(_x + dx + 1, _y + dy, queue, visited_queue)
            elif dx > 0:
                push_unique_pos(_x + dx + 1, _y + dy, queue, visited_queue)
            push_unique_pos(_x + dx, _y + dy, stack, visited_stack)
            push_unique_pos(_x + dx + 1, _y + dy, stack, visited_stack)
        elif board[_y][_x] == ']':
            if dx == 0:
                push_unique_pos(_x + dx, _y + dy, queue, visited_queue)
                push_unique_pos(_x + dx - 1, _y + dy, queue, visited_queue)
            elif dx < 0:
                push_unique_pos(_x + dx - 1, _y + dy, queue, visited_queue)
            push_unique_pos(_x + dx, _y + dy, stack, visited_stack)
            push_unique_pos(_x + dx - 1, _y + dy, stack, visited_stack)
        elif board[_y][_x] == '#':
            #print('There is a box faced the wall. Can\'t move.')
            return x, y
        #print('queue:', queue)
        #print('stack:', stack)
    
    #print('total stack:', stack)
    while stack:
        _x, _y = stack.pop()
        board[_y][_x], board[_y - dy][_x - dx] = board[_y - dy][_x - dx], board[_y][_x]
    #debug_board(board)

    return x + dx, y + dy


board = []
robot = None
for y, line in enumerate(sys.stdin):
    line = line.strip()
    
    if not line:
        break

    row = []
    for x, c in enumerate(line):
        if c == '@':
            row.extend(['.', '.'])
            robot = (x * 2, y)
        elif c == '.':
            row.extend(['.', '.'])
        elif c == '#':
            row.extend(['#', '#'])
        elif c == 'O':
            row.extend(['[', ']'])
    board.append(row)

#debug_board(board)

w, h = len(board[0]), len(board)

x, y = robot
for line in sys.stdin:
    operations = line.strip()
    for op in operations:
        dx, dy = DIRECTIONS[op]
        #print(f'move: ({x}, {y})')
        _x, _y = x + dx, y + dy

        if board[_y][_x] == '.':
            x, y = _x, _y
        elif board[_y][_x] == '[' or board[_y][_x] == ']':
            x, y = push_boxes(x, y, dx, dy, board)

#debug_board(board)

coordinates = 0
for y, row in enumerate(board):
    for x, c in enumerate(row):
        if c == '[':
            coordinates += 100 * y + x

print("Day 15 part 01 =>", coordinates)
