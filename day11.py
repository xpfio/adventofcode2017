def part1(s):
    directions = s.split(',')
    print(len(directions))

    cube_directions = {
        'ne':[+1, -1,  0],
        'n':[+1,  0, -1],
        'nw':[ 0, +1, -1],
        'sw':[-1, +1,  0],
        's':[-1,  0, +1],
        'se':[ 0, -1, +1]
    }

    x,y,z = 0,0,0
    for direction in directions:
        x += cube_directions[direction][0]
        y += cube_directions[direction][1]
        z += cube_directions[direction][2]
    
    print(x,y,z)
    return int((abs(x)+abs(y)+abs(z))/2)


def part2(s):
    directions = s.split(',')
    print(len(directions))

    cube_directions = {
        'ne':[+1, -1,  0],
        'n':[+1,  0, -1],
        'nw':[ 0, +1, -1],
        'sw':[-1, +1,  0],
        's':[-1,  0, +1],
        'se':[ 0, -1, +1]
    }

    x,y,z = 0,0,0
    maximum = 0
    for direction in directions:
        x += cube_directions[direction][0]
        y += cube_directions[direction][1]
        z += cube_directions[direction][2]
        maximum = max(maximum, int((abs(x)+abs(y)+abs(z))/2))

        # return int((abs(x)+abs(y)+abs(z))/2)
    return maximum


with open('input/day11.txt') as f:
    pb_input = f.read()
    print(part2(pb_input))