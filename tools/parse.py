def fromArrayInt(table,separator='\t'):
    rows = table.split('\n')
    output = []
    for row in rows:
        line = row.split(separator)
        line = list(map(lambda x: int(x), line))
        output.append(line)
    return output

# "5	1	9	5\n7	5	3\n2	4	6	8" -> [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]