"""Template file for Python source code"""
import math
from itertools import groupby

# PART 1
def part1(s):
    return sum([1 \
            for line in s.split('\n') \
            if len(set(line.split(' '))) == len(line.split(' ')) ])


def part2(s):
    return sum([1 \
            for line in s.split('\n') \
            if len(set(map(lambda x:''.join(sorted(x)),line.split(' ')))) == len(line.split(' ')) ])

# INPUTS
FILE = 'input/day04.txt'
TESTS_PART1 = [
    ('aa bb cc dd ee',1),
    ('aa bb cc dd aa',0),
    ('aa bb cc dd aaa\naa bb',2),
    ('aa bb cc dd aaa',1)
]

TESTS_PART2 = [
("abcde fghij", 1),
("abcde xyz ecdab", 0),
("a ab abc abd abf abj", 1),
("iiii oiii ooii oooi oooo", 1),
("oiii ioii iioi iiio", 0)
]


## Part 1 - Tests
def tests_part1(input, expected_solution):
    """Test Part 1 on the different inputs"""
    output = str(part1(str(input)))
    if str(expected_solution) == output:
        print('\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m')
    else:
        print('\033[91m' + 'NOPE\t', \
                'INPUT: ', input, \
                '\tOUTPUT: ', output, \
                '\tEXPECTED:', expected_solution, \
                '\033[0m')

for test in TESTS_PART1:
    tests_part1(test[0], test[1])

# Part 1 - Answer
def read_input():
    """Open Daily input file defined in FILE"""
    with open(FILE) as f:
        return f.read()

print('\033[94m' + 'PART 1 ANSWER: ', str(part1(str(read_input()))))
print('\n')


## Part 2 - Tests
def tests_part2(input, expected_solution):
    """Test Part 2 on the different inputs"""
    output = str(part2(str(input)))
    if str(expected_solution) == output:
        print('\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m')
    else:
        print('\033[91m' + 'NOPE\t', \
            'INPUT: ', input, \
            '\tOUTPUT: ', output, \
            '\tEXPECTED', expected_solution, \
            '\033[0m')

for test in TESTS_PART2:
    tests_part2(test[0], test[1])

# Part 2 - Answer
print('\033[94m' + 'PART 2 ANSWER: ', str(part2(str(read_input()))))
