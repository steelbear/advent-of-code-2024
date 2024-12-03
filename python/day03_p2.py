import sys
import re

pattern = re.compile('mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)')

result = 0
enabled = True
for line in sys.stdin:
    operand = pattern.findall(line)
    
    if operand:
        for a, b, do, dont in operand:
            if do:
                enabled = True
            elif dont:
                enabled = False
            elif enabled:
                result += int(a) * int(b)

print("day03 part01 =>", result)