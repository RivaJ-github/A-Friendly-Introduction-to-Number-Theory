from tools import gcd, phi, gcdWithXY, successive_square


''' 解同余式x^k≡b(mod m)'''
def solution(k, b, m):
    if gcd(b, m) != 1:
        raise Exception('b and m must be coprime')
    _phi = phi(m)
    (g, u, v) = gcdWithXY(k, _phi)
    if g != 1:
        raise Exception('k and phi(m) is not coprime')
    else:
        return successive_square(b, u, m)

if __name__ == '__main__':
    print(solution(113, 347, 463))
    print(solution(275, 139, 588))