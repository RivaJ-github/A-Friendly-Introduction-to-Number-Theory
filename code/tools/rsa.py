'''定义一系列RSA加密系统相关的静态函数'''
from .prime import gcdWithXY

def successive_square(a, k, m):
    ''' 逐次平方法解a^k(mod m) '''
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (b * a) % m
        a = a * a % m
        k = k // 2
    return b

class RSA:
    def __init__(self, m, k, _phi = 0):
        self.m = m
        self.k = k
        self._phi = _phi

    def encode(self, a):
        return successive_square(a, self.k, self.m)

    def decode(self, b):
        ''' 解码a的原文 '''
        if not self._phi:
            raise Exception('you should set privite key first') # only allow to decode when _phi is given
        (g, u, v) = gcdWithXY(self.k, self._phi)
        if g != 1:
            raise Exception('the public/privite key you give is not correct') # k or _phi are not coprime here
        else:
            return successive_square(b, u, self.m)

