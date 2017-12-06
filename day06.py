"""Template file for Python source code"""
import math
from itertools import groupby
import operator

# PART 1
def part1(s):
    banks = s.split('\t')
    banks = list(map(lambda x: int(x), banks))

    positions = []
    steps = 0

    while banks not in positions:
        # print(banks)
        positions.append(banks.copy())
        steps += 1
        index, value = max(enumerate(banks), key=operator.itemgetter(1))
        banks[index] = 0
        while value >= 1:
            index += 1
            index %= len(banks)
            banks[index] += 1
            value -= 1

    return steps


print(part1('0\t2\t7\t0'))
with open('input/day06.txt') as f:
    print(part1(f.read()))



# PART 1
def part2(s):
    banks = s.split('\t')
    banks = list(map(lambda x: int(x), banks))

    positions = []
    steps = 0

    while banks not in positions:
        # print(banks)
        positions.append(banks.copy())
        steps += 1
        index, value = max(enumerate(banks), key=operator.itemgetter(1))
        banks[index] = 0
        while value >= 1:
            index += 1
            index %= len(banks)
            banks[index] += 1
            value -= 1

    return steps - positions.index(banks) 


print(part2('0\t2\t7\t0'))
with open('input/day06.txt') as f:
    print(part2(f.read()))
