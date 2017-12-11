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




def algo(array_,to_reverse):
    array = array_.copy()
    position = 0
    skip_size = 0
    for k in range(64):
        for element in to_reverse:
            # print(array, element, position, skip_size)
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

        # print(array)
    return array

from functools import reduce

def part2(s):
    print(s)
    to_reverse = list(map(lambda x: ord(x),s))
    print(to_reverse)
    to_reverse = list(map(lambda x: int(x),to_reverse))
    to_reverse += [17, 31, 73, 47, 23]
    # print(to_reverse)
    array = list(range(256))
    array = algo(array, to_reverse)

    output = ''
    for index in range(16):
        sub_array = array[index*16:index*16+16]
        output += format(reduce((lambda x, y: x ^ y), sub_array), '02x')

    # format(10, '02x')
    return output

with open('input/day10.txt') as f:
    pb_input = f.read()
    print(part2(pb_input))