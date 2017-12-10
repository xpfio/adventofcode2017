import numpy as np

np.z

def day08 (s):
    # print(s)
    lines = s.split('\n')
    registry = {}
    for line in lines:
        [to_change, up_down, value, if_, from_, test_, value_test] = line.split(' ')
        if to_change not in registry:
            registry[to_change] = 0
        if from_ not in registry:
            registry[from_] = 0
        pass_test = eval(str(registry[from_]) + ' ' + test_ + ' ' + value_test)

        if pass_test:
            direction = 1 if up_down == 'inc' else -1
            registry[to_change] += int(value) * direction

        
    return max([registry[a] for a in registry])

def day08_2 (s):
    # print(s)
    lines = s.split('\n')
    registry = {}
    maximum = 0

    for line in lines:
        [to_change, up_down, value, if_, from_, test_, value_test] = line.split(' ')
        if to_change not in registry:
            registry[to_change] = 0
        if from_ not in registry:
            registry[from_] = 0
        pass_test = eval(str(registry[from_]) + ' ' + test_ + ' ' + value_test)

        if pass_test:
            direction = 1 if up_down == 'inc' else -1
            registry[to_change] += int(value) * direction

        
        maximum = max([maximum] + [registry[a] for a in registry])
    return maximum
        


with open('input/day08.txt') as f:
    s = f.read()
    print(day08(s))
    print(day08_2(s))