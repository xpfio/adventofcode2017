from tools import parse

# PART 1
def part1(s):
    return sum([max(i)-min(i) for i in parse.fromArrayInt(s)])

# PART 2
def part2(s):
    arr = parse.fromArrayInt(s)
    return sum([max([x//y for x in line for y in line if x%y==0]) for line in arr])


# INPUTS
FILE = 'input/day02.txt'
TESTS_PART1 = [
    ("5	1	9	5\n7	5	3\n2	4	6	8","18")
]
TESTS_PART2 = [
    ("5	9	2	8\n9	4	7	3\n3	8	6	5","9")
]


## Part 1 - Tests
def tests_part1(input, expected_solution):
    output = str(part1(str(input)))
    """Test Part 1 on the different inputs"""
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
print('\n')
