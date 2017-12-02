def fromArrayInt(table):
    rows = table.split('\n')
    output = []
    for row in rows:
        line = row.split('\t')
        line = list(map(lambda x: int(x), line))
        output.append(line)
    return output
