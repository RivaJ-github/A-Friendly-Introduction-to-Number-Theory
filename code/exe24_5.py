primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for p in primeList:
    print(f'&{p}', end='')
    a = 1
    flag = False
    while (a ** 2 < p):
        b = 0
        while b <= a and b ** 2 + a ** 2 <= p:
            c = 0
            while c <= b and c ** 2 + b ** 2 + a ** 2 <= p:
                if c ** 2 + b ** 2 + a ** 2 == p:
                    print(f'={a}^2+{b}^2+{c}^2', end='')
                    flag = True
                c += 1
            b += 1
        a += 1
    if not flag:
        print('=None', end='')
    print('\\\\')