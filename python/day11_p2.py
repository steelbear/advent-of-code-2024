import sys
from time import time

def len_digit(num):
    i = 0
    pos = 1
    while pos <= num:
        i += 1
        pos *= 10
    return i


def blink(target_stone, limit, memory_nums, memory_blinked):
    stack = [(target_stone, limit)]
    while stack:
        stone, age = stack[-1]
        # 몇번의 깜박임 후에 몇개의 돌이 존재하는지 이미 아는 경우
        if memory_nums.get((stone, age)):
            stack.pop()
        # 몇개의 돌이 있을진 몰라도 이 돌이 깜박임 후에 어떻게 변하는지 아는 경우
        elif memory_blinked.get(stone):
            if age == 1:
                memory_nums[(stone, age)] = len(memory_blinked[stone])
                continue
            found = True
            amount = 0
            for splitted in memory_blinked[stone]:
                if memory_nums.get((splitted, age - 1)):
                    amount += memory_nums[(splitted, age - 1)]
                else:
                    stack.append((splitted, age - 1))
                    found = False
            if found:
                memory_nums[(stone, age)] = amount
        # 이 돌이 깜박임 후에 어떻게 변할지 모르는 경우
        elif len_digit(stone) % 2 == 0:
            half_len = (len_digit(stone) // 2)
            left_stone = stone // (10 ** half_len)
            right_stone = stone % (10 ** half_len)
            memory_blinked[stone] = [left_stone, right_stone]
        else:
            memory_blinked[stone] = [stone * 2024]
    return memory_nums[(target_stone, limit)]


line = sys.stdin.readline()
stones = list(map(int, line.strip().split()))
memory_nums = { (0, 1): 1 }
memory_blinked = { 0: [1] }

nums_blinked = 0
for stone in stones:
    nums_blinked += blink(stone, 75, memory_nums, memory_blinked)

print("day11 part02 =>", nums_blinked)
