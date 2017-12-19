from day10 import knot_hash

print(knot_hash('test'))

def hex_to_bin(s):
    mapping = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'a':'1010',
        'b':'1011',
        'c':'1100',
        'd':'1101',
        'e':'1110',
        'f':'1111'
    }
    output = ''
    for a in s:
        output += mapping[a]
    return output

print(hex_to_bin('a0c2017'))

# Part 1
# with open('input/day14.txt') as input_file:
#     string = input_file.read()
#     total = 0
#     for a in range(128):
#         row = string + '-' + str(a)
#         hash_ = knot_hash(row)
#         bits = hex_to_bin(hash_)
#         print(hash_,bits)
#         total += sum([1 for a in bits if a == '1'])
#     print(total)
    

# Part 2
with open('input/day14.txt') as input_file:
    string = input_file.read()
    array = []

    for a in range(128):
        row = string + '-' + str(a)
        hash_ = knot_hash(row)
        bits = hex_to_bin(hash_)
        array.append(bits)
        
    # print(array)

    regions = 0
    to_explore = []
    explored = []

    for index1, row in enumerate(array):
        for index2, value in enumerate(list(row)):
            if (index1,index2) not in explored and value == '1':
                print(index1,index2)
                to_explore = [(index1,index2)]
                while len(to_explore) > 0:
                    explored.append((index1,index2))
                    current = to_explore.pop()
                    x = current[0]
                    y = current[1]
                    
                    if x > 0 and array[x-1][y] == '1' and (x-1,y) not in explored:
                        to_explore.append((x-1,y))

                    if x < len(array) - 1 and array[x+1][y] == '1' and (x+1,y) not in explored:
                        to_explore.append((x+1,y))

                    if y > 0 and array[x][y-1] == '1' and (x,y-1) not in explored:
                        to_explore.append((x,y-1))

                    if y < len(array) - 1 and array[x][y+1] == '1' and (x,y+1) not in explored:
                        to_explore.append((x,y+1))

                    print(to_explore)

            regions += 1
            

    print(regions)


