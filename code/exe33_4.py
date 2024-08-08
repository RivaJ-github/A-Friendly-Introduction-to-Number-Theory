import math
from tools import gcd

factor = math.sqrt(2)
for y in range (12, 5000):
    (frac, x) = math.modf(factor * y)
    if (frac > 0.5):
        frac = 1 - frac
        x += 1
    if y * frac < 1:
        print(f'{int(x)} & {y} & {frac:.8f} & {y * frac:.8f} & {(y ** 2 * frac):.2f} \\\\')