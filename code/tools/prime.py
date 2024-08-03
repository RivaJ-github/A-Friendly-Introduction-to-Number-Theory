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

def JacobiSymbol(a, b):
    '''计算雅可比符号(a/b)'''
    # 忽略参数校验，假设初始参数都是正奇数
    if (a == 2):
        return 1 if b % 8 == 1 or b % 8 == 7 else -1

    flag = False    # 去除因子2
    while (a % 2 == 0):
        a //= 2
        flag = not flag

    res = JacobiSymbol(2, b) if flag else 1

    if (a == 1):
        return res

    return res * JacobiSymbol(b % a, a)

def DesentProcedure(A, B, p):
    ''' 
    二次递降程序
    start from A^2 + B^2 \equiv (mod p)
    @return (u, v) 满足a^2 + b^2 = p
    '''
    M = (A**2 + B**2) // p
    while (M > 1):
        u = A % M
        if (u > M // 2):
            u -= M
        v = B % M
        if (v > M // 2):
            v -= M
        r = (u**2 + v**2) // M
        A, B = abs(A*u + B*v) // M, abs(A*v - B*u) // M
        M = r
    return (A, B)

def DesentProcedure_1(p):
    ''' 
    对满足p模8余5的p进行二次递降程序
    @return (x, y) 满足x^2 + y^2 = p
    '''
    A = (-2 * successive_square(-4, (p-5)//8, p)) % p
    return DesentProcedure(A, 1, p)

def DesentProcedure_2(n):
    '''
    利用二次递降程序分解n
    @return (x, y) 满足x^2 + y^2 = n
    '''
    factors = factoringPrimeFactors(n)
    c = 1 # x, y的公因数
    x, y = 0, 1
    for f in factors:
        (p, r) = f
        c = p ** (r // 2)
        if (r % 2 == 1):
            if p % 4 == 3:
                raise Exception('n cannot be decomposed into a sum of squares')
            while True:
                a = random.randint(2, p)
                if JacobiSymbol(a, p) == -1:
                    A = successive_square(a, (p-1)//4, p)
                    if (A != 1): # 不知道为什么会出现1
                        break
                else:
                    print('Can false?')
            u, v = DesentProcedure(A, 1, p)
            x, y = x * u + y * v, abs(x * v - y * u)
    return (x * c, y * c)
