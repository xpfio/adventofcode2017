def day9(s,current_depth=1):
    print('DAY9',s)
    index = 0
    total = 0
    ignored = False
    ignore_next = False

    while index < len(s):
        if ignore_next:
            ignore_next = False
            index += 1
            continue

        if s[index] == '{' and not ignored:
            end = index + day9(s[index+1:],current_depth+1)[0]
            print('IDX',index,end)
            total += current_depth + day9(s[index+1:end+1],current_depth+1)[1]
            print('BLOCK',s[index:end+2], current_depth, total)
            index = end + 1
        elif s[index] == '}' and not ignored:
            return [index,total]
        elif s[index] == '<' and not ignored:
            ignored = True
        elif s[index] == '>':
            ignored = False
        elif s[index] == '!':
            ignore_next = True
            
        index += 1
    return [index,total]


with open('input/day09.txt') as f:
    s = f.read()
    print(day9(s))


