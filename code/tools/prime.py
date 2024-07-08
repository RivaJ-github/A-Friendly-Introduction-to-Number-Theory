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
    while (x <= 0):
        x += b
    return (g, x, (g - a * x) // b)


def LCM(m, n):
    return m // gcd(m, n) * n 

if __name__ == '__main__':
    # print(isPrime(316258250, 1160718174))
    # print(factoringPrimeFactors(12))
    # # print(gcd(0, 0))
    # def exe_5_4_a(m, n):
    #     print(f'LCM({m}, {n}) = {LCM(m, n)}')
    # exe_5_4_a(8, 12)
    # exe_5_4_a(20, 30)
    # exe_5_4_a(51, 68)
    # exe_5_4_a(23, 18)
    # exe_5_4_a(301337, 307829)
    print(gcdWithXY(301337, 307829))
