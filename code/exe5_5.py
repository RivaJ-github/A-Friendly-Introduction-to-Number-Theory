from tools.prime import gcd

def solution(n):
    s = set()
    while (n not in s):
        s.add(n)
        stop = n
        n = n // 2 if n % 2 == 0 else n * 3 + 1
    return (stop, len(s))


if __name__ == '__main__':
    # print(solution(21))
    # print(solution(13))
    # print(solution(31))
    # print(solution(12))
    # print(solution(13))
    # for i in range(1, 101):
        # print(solution(i)) 
        # print(f'$T({i})={solution(i)}$')
    result = [f'$T({i})={solution(i)[1]}$' for i in range(1, 101)]
    rows = [' & '.join(result[i: i+8]) + '\\\\' for i in range(0, len(result), 8)]
    formated_output = '\n'.join(rows)
    print(formated_output)
