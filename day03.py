"""Template file for Python source code"""
import math

# a = s.split('\n')
# a = [ for i in ]
# sum(a)
# C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
# any()
# all()

# PART 1
def part1(s):
    n = int(s)-1
    m = math.ceil(math.sqrt(n))
    k = (m-1)/2 if m%2 == 1 else (m/2 if n>=m*(m+1) else m/2 - 1)

    if n <= (2*k+1)**2:
        return int(abs(n-4*k**2-3*k)+abs(k))
    elif n <= 2*(k+1)*(2*k+1):
        return int(abs(k+1)+abs(4*k**2+5*k+1-n))
    elif n<= 4*(k+1)**2:
        return int(abs(4*k**2+7*k+3-n)+abs(-k-1))
    else:
        return int(abs(-k-1)+abs(n-4*k**2-9*k-5))

# PART 2
def part2(s):
    n = int(s)
    spiral = {}
    value = 1
    x = 0
    y = 0

    #Init
    spiral[(x,y)] = value
    x += 1

    while value <= n:
        value = 0
        # Check neighbors
        to_check = [
            (x+1,y+1),
            (x+1,y),
            (x+1,y-1),
            (x,y+1),
            # (x,y),
            (x,y-1),
            (x-1,y+1),
            (x-1,y),
            (x-1,y-1),
        ]
        for a in to_check:
            if a in spiral:
                value += spiral[a]
        spiral[(x,y)] = value

        # Move
        to_check = [
            (x-1,y),
            (x,y+1),
            (x+1,y),
            (x,y-1)
        ]
        direction = ''
        for a in to_check:
            if a in spiral:
                direction += '1'
            else:
                direction += '0'
        
        if direction == '1000':
            y = y+1
        elif direction == '0001':
            x = x -1
        elif direction == '0011':
            x = x-1
        elif direction == '0010':
            y = y-1
        elif direction == '0110':
            y = y-1
        elif direction == '0100':
            x = x+1
        elif direction == '1100':
            x = x+1
        elif direction == '1001':
            y = y+1

    return value


# INPUTS
FILE = 'input/day03.txt'
TESTS_PART1 = [
    (1,0),
    (12,3),
    (23,2),
    (1024,31),
    (325489,552)
]
TESTS_PART2 = [
    (800,806)
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

## Part 2 - Answer
print('\033[94m' + 'PART 2 ANSWER: ', str(part2(str(read_input()))))
