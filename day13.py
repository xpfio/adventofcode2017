def part1(s):
    lines = s.split('\n')
    total = 0
    for line in lines:
        print(line)
        depth = int(line.split(': ')[0])
        range_ = int(line.split(': ')[1])
        if (depth) % (2 * range_ - 2) == 0:
            print(depth,range_)
            total += depth * range_ 
            
    return total

with open('input/day13.txt', 'r') as input_file:
    print(part1('''0: 3
1: 2
4: 4
6: 4'''))
    print (part1(input_file.read()))


def part2(s):
    lines = s.split('\n')
    total = 0

    data = []
    for line in lines:
        depth = int(line.split(': ')[0])
        range_ = int(line.split(': ')[1])
        data.append({
            'depth': depth,
            'range_': range_
        })

    while any([(line['depth'] + total) % (2 * line['range_'] - 2) == 0 for line in data]):
        total += 1

    return total

with open('input/day13.txt', 'r') as input_file:
    print(part2('''0: 3
1: 2
4: 4
6: 4'''))
    print (part2(input_file.read()))
