from tools.prime import gcd

def solution(a, b):
    print(f'\gcd({a}, {b})= {gcd(a, b)}')

def format(res):
    return f'{res[0]}^2 + {res[1]}^2'

if __name__ == '__main__':
    solution(12345, 67890)
    solution(54321, 9876)
