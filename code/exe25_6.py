import math

for m in (10, 70, 130, 1105):
    res = []
    b = 0
    while (b**2 <= m//2):
        a = int(math.sqrt(m - b**2))
        if (a**2 + b**2 == m):
            res.append((a, b))
        b+=1
    print(f'S({m})={len(res)}', end = '')
    if (len(res)):
        print('\\quad n', end = '')
        for item in res:
            print(f'={item[0]}^2+{item[1]}^2', end = '')
    print()