"""Template file for Python source code"""
import math
from itertools import groupby
import operator

# PART 1
def get_info(s):
    data = {}
    rows = s.split('\n')
    for row in rows:
        extract1 = row.split(' -> ')
        # print(extract1)
        name = extract1[0].split(' ')[0]
        weight = extract1[0].split('(')[1].split(')')[0]
        if len(extract1) > 1:
            subtree = extract1[1].split(', ')
            # print(name,weight,subtree)
            current = {
                'name':name,
                'weight':int(weight),
                'subtree':subtree
            }
            data[name] = current
        else:
            subtree = []
            # print(name,weight,subtree)
            current = {
                'name':name,
                'weight':int(weight),
                'subtree':subtree
            }
            data[name] = current

    return data

def get_weight(node,data2):
    # print(str(node))
    # print(data2[node])
    if len(data2[node]['subtree']) == 0:
        return data2[node]['weight']
    else:
        return data2[node]['weight'] + sum([get_weight(k,data2) for k in data2[node]['subtree']])


with open('input/day07.txt') as f:
    data = get_info(f.read())
    for k in data:
        if len(data[k]['subtree']) > 0:
            if len(set([get_weight(a,data) for a in data[k]['subtree']])) > 1:
                # print('A')
                print(k, [get_weight(a,data) for a in data[k]['subtree']])
