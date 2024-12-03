import sys
import re

mul_pattern = re.compile('mul\((\d+),(\d+)\)')

result = 0
for line in sys.stdin:
    mul_operand = mul_pattern.findall(line)
    
    if mul_operand:
        for a, b in mul_operand:
            result += int(a) * int(b)

print("day03 part01 =>", result)