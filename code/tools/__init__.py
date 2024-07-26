from .prime import *
from .congruence import *

''' a^k(mod m) '''
def successive_square(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (b * a) % m
        a = a * a % m
        k = k // 2
    return b