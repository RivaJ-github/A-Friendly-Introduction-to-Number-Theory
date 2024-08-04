from .prime import gcdWithXY
from .prime import factoringPrimeFactors

'''
    返回与x同余的最小正整数。
'''
def minimize(x, m):
    return x - (x // m) * m

'''
    解线性同余式ax≡b(mod m)
    return [x_1, ... x_n]
'''
def linearCongruence(a, c, m):
    (g, u, _) = gcdWithXY(a, m)
    if c % g == 0:
        x = minimize(c // g * u, m // g)
        return [x + k * m // g for k in range(0, g)]
    # 无解返回空列表
    return []

