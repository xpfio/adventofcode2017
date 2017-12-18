step = 367
# step = 3

array = [0]
current_position = 0

for k in range(1,2017+1):
    current_position += step
    current_position %= len(array)
    array = array[:current_position+1] + [k] + array[current_position+1:]
    current_position += 1
    print(current_position,array)

print(array[current_position+1])