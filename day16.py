with open('input/day16.txt') as input_file:
    data = input_file.read()
    # data = 's1,x3/4,pe/b'
    data = data.split(',')

    state = list('abcdefghijklmnop')
    print(state)
    for instruction in data:

        if instruction[0] == 's':
            number = int(instruction[1:])
            state = state[len(state)-number:len(state)] + state[0:len(state)-number]

        elif instruction[0] == 'x':
            x = int(instruction[1:].split('/')[0])
            y = int(instruction[1:].split('/')[1])
            temp = state[x]
            # print(x,y, temp,state)
            state[x] = state[y]
            state[y] = temp

        elif instruction[0] == 'p':
            x = str(instruction[1:].split('/')[0])
            y = str(instruction[1:].split('/')[1])

            x_index = state.index(x)
            y_index = state.index(y)
 
            state[x_index] = y
            state[y_index] = x
            
        print(''.join(state))