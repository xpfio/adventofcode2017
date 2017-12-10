def day10(s):
    print(s)
    to_reverse = s.split(',')
    to_reverse = list(map(lambda x: int(x),to_reverse))
    # print(to_reverse)
    array = list(range(256))

    position = 0
    skip_size = 0
    for element in to_reverse:
        print(array, element, position, skip_size)
        copy = array.copy()
        for index in range(element):
            from_index = position+index
            from_index %= len(array)

            to_index = (position+element-1) - index
            to_index %= len(array)

            array[from_index] = copy[to_index]

        position += (element + skip_size)
        position %= len(array)
        skip_size += 1

    print(array)
    return array[0]*array[1]

    

with open('input/day10.txt') as f:
    pb_input = f.read()
    print(day10(pb_input))



def algo(array_,to_reverse):
    array = array_.copy()
    position = 0
    skip_size = 0
    for k in range(64):
        for element in to_reverse:
            print(array, element, position, skip_size)
            copy = array.copy()
            for index in range(element):
                from_index = position+index
                from_index %= len(array)

                to_index = (position+element-1) - index
                to_index %= len(array)

                array[from_index] = copy[to_index]

            position += (element + skip_size)
            position %= len(array)
            skip_size += 1

        print(array)
    return array