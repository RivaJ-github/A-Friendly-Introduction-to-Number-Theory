from tools import gcdWithXY, minCongruence

def solution(b, m, c, n):
    (g, u, _) = gcdWithXY(m, n)
    if (g != 1):
        raise Exception("gcd(m, n) != 1")
    x = b + u * (c - b) * m
    return minCongruence(x, n * m)

if __name__ == '__main__':
    res = solution(1, 2, 3, 5)
    print(res)
    