from tools import JacobiSymbol, successive_square

def solution(a, p):
    if JacobiSymbol(a, p) != 1:
        raise ValueError('a is not a quadratic residue of p')
    if successive_square(a, (p - 1) // 4, p) == 1:
        return successive_square(a, (p + 3) // 8, p)
    else:
        return 2 * a * successive_square(4 * a, (p - 5) // 8, p) % p

if __name__ == '__main__':
    print(solution(17, 1021))
    print(solution(23, 1021))
    # print(solution(31, 1021))
