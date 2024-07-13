from tools import linearCongruence

def solution(m, f):
    res = []
    for x in range(0, m):
        s = 0
        for item in f:
            s += item[0] * x ** item[1]
        if s % m == 0:
            res.append(x)
    return res

if __name__ == '__main__':
    for m in [130, 137, 144, 151, 158, 165, 172]:
        print(m)
        print(solution(m, [[1, 11], [21, 7], [-8, 3], [8, 0]]))
