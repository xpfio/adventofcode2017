# PART 1
def part1(input):
    """Calculate Part 1 of the problem for any input"""
    #
    # code goes here
    #
    return 'OUTPUT_'

# PART 2
def part2(input):
    """Calculate Part 2 of the problem for any input"""
    #
    # code goes here
    #
    return 'OUTPUT_'

# INPUTS

FILE = 'input/day02.txt'
TESTS_PART1 = [
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT")
]
TESTS_PART2 = [
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT"),
    ("INPUT","OUTPUT")
]




## Part 1 - Tests
def tests_part1(input, expected_solution):
    """Test Part 1 on the different inputs"""
    if str(expected_solution) == str(part1(str(input))):
        print('\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m')
    else:
        print('\033[91m' + 'NOPE\t', \
                'INPUT: ', input, \
                '\tOUTPUT: ', str(part1(str(input))), \
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
    if str(expected_solution) == str(part2(str(input))):
        print('\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m')
    else:
        print('\033[91m' + 'NOPE\t', \
            'INPUT: ', input, \
            '\tOUTPUT: ', str(part2(str(input))), \
            '\tEXPECTED', expected_solution, \
            '\033[0m')

for test in TESTS_PART2:
    tests_part1(test[0], test[1])

## Part 2 - Answer
print('\033[94m' + 'PART 2 ANSWER: ', str(part2(str(read_input()))))
