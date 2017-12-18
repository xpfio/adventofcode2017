with open('input/day18.txt') as input_file:
    lines = input_file.read().split('\n')

    register = {}
    for a in list('abcdefghijklmnopqrstuvwxyz'):
        register[a] = 0
    step = 0
    last_sound = ''

    while step >= 0 and step < len(lines):
        instruction = lines[step]
        # print(instruction)

        if instruction[0:3] == 'snd':
            value = instruction[4:]
            if value in register:
                value = register[value]
            else:
                value = int(value)
            last_sound = value

        if instruction[0:3] == 'set':
            X = instruction[4:].split(' ')[0]
            Y = instruction[4:].split(' ')[1]
            if Y in register:
                Y = register[Y]
            else:
                Y = int(Y)
            register[X] = Y
        
        if instruction[0:3] == 'add':
            X = instruction[4:].split(' ')[0]
            Y = instruction[4:].split(' ')[1]
            if Y in register:
                Y = register[Y]
            else:
                Y = int(Y)
            register[X] += Y

        if instruction[0:3] == 'mul':
            X = instruction[4:].split(' ')[0]
            Y = instruction[4:].split(' ')[1]
            if Y in register:
                Y = register[Y]
            else:
                Y = int(Y)
            register[X] *= Y    

        if instruction[0:3] == 'mod':
            X = instruction[4:].split(' ')[0]
            Y = instruction[4:].split(' ')[1]
            if Y in register:
                Y = register[Y]
            else:
                Y = int(Y)
            register[X] %= Y        

        if instruction[0:3] == 'rcv':
            X = instruction[4:]
            if X in register:
                X = register[X]
            else:
                X = int(X)
            if X != 0:
                print(last_sound)
                if last_sound != 0:
                    step = -2

        if instruction[0:3] == 'jgz':
            X = instruction[4:].split(' ')[0]
            Y = instruction[4:].split(' ')[1]
            if X in register:
                X = register[X]
            else:
                X = int(X)
            if Y in register:
                Y = register[Y]
            else:
                Y = int(Y)
                
            if X > 0:
                step += Y - 1

        step += 1