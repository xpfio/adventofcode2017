# PART 1
def part1(input):
    return sum([int(input[i]) for i in range(len(input)) if input[i-1] == input[i]])

# PART 2
def part2(input):
    n = len(input)
    return sum([int(input[i]) for i in range(n) if input[i] == input[(i+n//2) % n]])





## Part 1 - Tests
def tests_part1(input, expected_solution):
    if str(expected_solution) == str(part1(str(input))):
        print '\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m'
    else:
        print '\033[91m' + 'NOPE\tINPUT: ', input, '\tOUTPUT: ', str(part1(str(input))), '\tEXPECTED', expected_solution,'\033[0m'

tests_part1(1122,3)
tests_part1(1111,4)
tests_part1(1234,0)
tests_part1(91212129,9)


## Part 1 - Answer
def read_input():
    with open('input/day01.txt') as f:
        return f.read()
        
print '\033[94m' + 'PART 1 ANSWER: ', str(part1(str(read_input())))
print('\n')



## Part 2 - Tests
def tests_part2(input, expected_solution):
    if str(expected_solution) == str(part2(str(input))):
        print '\033[92m' + 'GOOD\tINPUT: ', input, '\tOUTPUT: ', expected_solution, '\033[0m'
    else:
        print '\033[91m' + 'NOPE\tINPUT: ', input, '\tOUTPUT: ', str(part2(str(input))), '\tEXPECTED', expected_solution,'\033[0m'


tests_part2(1212, 6)
tests_part2(1221, 0)
tests_part2(123425, 4)
tests_part2(123123, 12)
tests_part2(12131415, 4)

## Part 2 - Answer
print '\033[94m' + 'PART 2 ANSWER: ', str(part2(str(read_input())))

    