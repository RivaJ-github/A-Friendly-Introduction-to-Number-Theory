import math
import random

'''
两数是否互素
'''
def isPrime(a, b):
    return gcd(a, b) == 1

'''
分解质因素：
TODO: It's slow! Do it better!
'''
def factoringPrimeFactors(n):
    res = []
    p = 2
    while (n > 1):
        c = 0
        while (n % p == 0):
            c += 1
            n //= p
        if (c > 0):
            res.append((p, c))
        p += 1
    return res

'''
最大公约数(欧几里得算法)
'''
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)   

'''
求正余数
'''
def minCongruence(a, b):
    if (b < 0):
        raise Exception('b must be a positive integer')
    return a - math.floor(a / b) * b 

'''
解ax+by=gcd(a,b)
返回(g, x, y)
'''
def gcdWithXY(a, b):
    if (b == 0):
        return (a, 1, 0)
    x, g, v, w = 1, a, 0, b
    while (w != 0):
        t = g % w
        q = g // w
        s = x - q * v
        x, g = v, w
        v, w = s, t
    
    x = minCongruence(x, b) 
    return (g, x, (g - a * x) // b)


def LCM(m, n):
    return m // gcd(m, n) * n 

def sigma(n):
    factors = factoringPrimeFactors(n)
    res = 1
    for factor in factors:
        res *= factor[0] ** (factor[1] + 1) - 1
        res //= factor[0] - 1
    return res

def isCarmichael(n):
    '''判断n是否是卡米歇尔数'''
    factors = factoringPrimeFactors(n)
    if len(factors) == 1:
        return False
    for factor in factors:
        if (factor[1] > 1) or (n-1) % (factor[0] - 1) != 0:
            return False
    return True

def RabinMillerTest(n, times = 10):
    '''
    合数的拉宾-米勒测试
    @param n: 待测试合数
    @param times: 测试次数
    @return: 是否是合数（True则一定是合数，False则大概率是合数）
    '''
    k = 0
    q = n - 1
    while (q % 2 == 0):
        q //= 2
        k += 1
    for i in range (0, times):
        a = random.randint(2, n-2)
        ss = successive_square(a, q, n)
        if (ss == 1 or ss == n - 1): 
            return False
        for j in range(1, k):
            ss = ss * 2 // n
            if (ss == -1):
                return False
    return True

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

def quadratic_residue(p):
    '''计算素数p的二次剩余列表'''
    res = []
    for a in range(1, (p+1)//2):
        res.append(a**2 % p)
    return res