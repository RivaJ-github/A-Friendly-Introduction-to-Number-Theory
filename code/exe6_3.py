from tools.prime import gcdWithXY

def solution(a, b):
    res = gcdWithXY(a, b)
    print(f'\gcd({a}, {b}) = {res[0]}，(x,y)=({res[1]},{res[2]})')

if __name__ == '__main__':
    solution(19789, 23548)
    solution(31875, 8387)
    solution(22241739, 19848039)
