def part1(s):
    lines = s.split('\n')
    to_explore = [0]
    group_0 = []
    
    while len(to_explore) > 0:
        current = to_explore.pop()
        data = lines[current].split(' <-> ')[1]
        data = data.split(',')
        data = list(map(int,data))
        
        for a in data:
            if a not in group_0:
                group_0.append(a)
                to_explore.append(a)
        
    return len(group_0)

def part2(s):
    lines = s.split('\n')
    to_explore = [0]
    groups = []
    nb_groups = 0

    for x in range(len(lines)):
        if not x in groups:
            nb_groups += 1
            to_explore = [x]
            while len(to_explore) > 0:
                current = to_explore.pop()
                data = lines[current].split(' <-> ')[1]
                data = data.split(',')
                data = list(map(int,data))
                
                for a in data:
                    if a not in groups:
                        groups.append(a)
                        to_explore.append(a)
        
    return nb_groups

with open('input/day12.txt') as f:
    pb_input = f.read()
    print(part1(pb_input))
    print(part2(pb_input))