from tools.prime import gcdWithXY

def sigma(n):
    res = 0
    a = 1
    b = n
    while a <= b and 2 * a < n:
        if (n % a == 0):
            res += a + b
        a += 1
        b = n // a
    return res
        

if __name__ == '__main__':
    print(sigma(10))
    print(sigma(20))
    print(sigma(25))
    print(sigma(1728))
