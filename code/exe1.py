def try_to_find_next_2_results():
    m = 9
    n = 6
    result = []
    while result.__len__() < 2:
        square = m * m
        trigonometric = n * (n + 1) / 2
        if square == trigonometric :
            result.append([m, n, square])
            n += 1
            m += 1
        elif square > trigonometric:
            n += 1
        else:
            m += 1
    return result

if __name__ == '__main__':
    result = try_to_find_next_2_results()
    for i in range(result.__len__()):
        print(f'{result[i][0]} * {result[i][0]} = {result[i][1]} * ({result[i][1]} + {result[i][1]}) = {result[i][2]}')