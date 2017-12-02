"""Template file for Python source code"""

# a = s.split('\n')
# a = [ for i in ]
# sum(a)
# C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
# any()
# all()

# PART 1
def part1(s):
    """Calculate Part 1 of the problem for any input"""
    #
    # code goes here
    #
    return 'OUTPUT'

# PART 2
def part2(s):
    """Calculate Part 2 of the problem for any input"""
    #
    # code goes here
    #
    return 'OUTPUT_'


# INPUTS
FILE = 'input/day02.txt'
TESTS_PART1 = [
    ("INPUT","OUTPUT")
]
TESTS_PART2 = [
    ("INPUT","OUTPUT")
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

## Part 1 - Answer
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

## Part 2 - Answer
print('\033[94m' + 'PART 2 ANSWER: ', str(part2(str(read_input()))))
