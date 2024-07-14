import math

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
求最大公约数以及ax+by=gcd(a,b)的解
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
    
    x -= math.floor(x / b) * b 
    return (g, x, (g - a * x) // b)


def LCM(m, n):
    return m // gcd(m, n) * n 

if __name__ == '__main__':
    # print(gcd(1547, 6731))
    print(factoringPrimeFactors(52633))
    # # print(gcd(0, 0))
    # def exe_5_4_a(m, n):
    #     print(f'LCM({m}, {n}) = {LCM(m, n)}')
    # exe_5_4_a(8, 12)
    # exe_5_4_a(20, 30)
    # exe_5_4_a(51, 68)
    # exe_5_4_a(23, 18)
    # exe_5_4_a(301337, 307829)
    # print(gcdWithXY(37, 47))
    # res = [2]
    # n = 3
    # while len(res) < 100:
    #     flag = True
    #     for p in res:
    #         if not isPrime(n, p):
    #             flag = False
    #             break
    #     if flag:
    #         res.append(n)
    #     n+=2
    # print(res)
