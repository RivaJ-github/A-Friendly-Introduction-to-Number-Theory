def getNextSolution(originPoint):
    u, v = originPoint
    return ((2*v**2+u**2), (2*u*v))


if __name__ == '__main__':
    solve = (3, 2)
    res = [solve]
    for i in range(3):
        solve = getNextSolution(solve)
        res.append(solve)
    print(f'整数解：{res}')
    
    # makeTable
    print('$x$ & $y$ & $n$ & $m$ & $m^2$ \\\\')
    for item in res:
        x, y = item
        print(f'{x} & {y} & {x - 1} & {y // 2} & {(y // 2) **2} \\\\')