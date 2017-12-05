"""Template file for Python source code"""
import math
from itertools import groupby

# PART 1
def part1(s):
    row = s.split('\n')
    row = list(map(lambda x: int(x), row))

    steps = 0 
    position = 0
    while position >= 0 and position < len(row):
        current = row[position]
        row[position] +=1
        position += current
        steps +=1
    
    return steps

def part2(s):
    row = s.split('\n')
    row = list(map(lambda x: int(x), row))
    
    steps = 0 
    position = 0
    while position >= 0 and position < len(row):
        current = row[position]
        if current >= 3:
            row[position] -= 1
        else:
            row[position] +=1
            
        position += current
        steps +=1
    
    return steps


# INPUTS
FILE = 'input/day05.txt'
TESTS_PART1 = [('0\n3\n0\n1\n-3',5)]
TESTS_PART2 = [('0\n3\n0\n1\n-3',10)]


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
