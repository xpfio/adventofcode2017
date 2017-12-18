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

with open('input/day14.txt') as input_file:
    string = input_file.read()
    total = 0
    for a in range(128):
        row = string + '-' + str(a)
        hash_ = knot_hash(row)
        bits = hex_to_bin(hash_)
        print(hash_,bits)
        total += sum([1 for a in bits if a == '1'])
    print(total)