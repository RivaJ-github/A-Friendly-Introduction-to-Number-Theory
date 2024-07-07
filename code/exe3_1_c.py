def getTable(target_length = 10):
    res = []
    for u in range(2, 11):
        row = []
        res.append(row)
        for v in range(1, u):
            row.append((u**2 - v**2, 2*u*v, u**2 + v**2))
    return res


if __name__ == '__main__':
    result = getTable(20)
    formatted_output = ' \\\\\n'.join([' & '.join(map(str, row)) for row in result])
    print(formatted_output)