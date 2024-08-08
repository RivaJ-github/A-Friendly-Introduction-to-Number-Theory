import math
from tools import gcd

''' (a) '''
gamma = (1 + math.sqrt(5)) / 2
print()
diff = 1
for i in range(1, 21):
    (frac, n) = math.modf(gamma * i)
    if frac > 0.5:
        frac = 1 - frac
        n += 1
    if frac < diff:
        diff = frac
        x = n
        y = i
print(x, y, x / y)

''' (b) '''
for y in range(22, 1001):
    (frac, x) = math.modf(gamma * y)
    if frac > 0.5:
        frac = 1 - frac
        x += 1
    if frac < 1 / y and gcd(x, y) == 1:
        print(f'${int(x)}$ & ${y}$ & ${frac*y:.6f}$ & ${x/y:.10f}$ \\\\')
        print('\\hline')

''' (c) '''
fibs = [1, 1]
for i in range(2, 41):
    fibs.append(fibs[i - 1] + fibs[i - 2])

for i in [20, 30, 40]:
    diff = math.fabs(fibs[i] / fibs[i - 1] - gamma)
    print(f'{diff:.25f}')