import sys
from time import time

def isPositiveInteger(n):
    return isinstance(n, int) and n > 0

def verifyPositiveInteger(n):
    if not isPositiveInteger(n):
        raise ValueError('The param must be a positive integer')


def solution_a(n):
    verifyPositiveInteger(n)
    res = ([], [])
    p = 2
    while (n > 1):
        count = 0
        while n % p == 0:
            count += 1
            n = n // p
        if count > 0:
            res[0].append(p)
            res[1].append(count)
        p += 1
    return res


def solution_b(n):
    verifyPositiveInteger(n)
    res = ([], [])
    # You may use a larger initial prime pool.
    primePool = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 
        131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 
        359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 
        479, 487, 491, 499, 503, 509, 521, 523, 541
    ]
    i = 0
    p = primePool[i]
    while (n > 1):
        count = 0
        while n % p == 0:
            count += 1
            n = n // p
        if count > 0:
            res[0].append(p)
            res[1].append(count)
        if (i < 100):
            p = primePool[i] # use prime pool to optimize
            i += 1
        elif p * p > n: # the most efficient optimize which accelerated the algorithm by 500 times
            p = n
        else:
            p += 2 # another optimize
    return res

def formatItem(sol):
    return ' \cdot '.join([str(sol[0][i]) + ('^{' + str(sol[1][i]) + '}' if sol[1][i] > 1 else '') for i in range(0, len(sol[0]))])

def print_beauty(res):
    print('\\begin{tabular}{ll}\n\\centering')
    for i in range(0, 15):
        print(f"${i+1000000}={formatItem(res[i])}$ & ${i+1000016}={formatItem(res[i])}$ \\\\")
    print(f"${1000016}={formatItem(res[16])}$ & \\\\")
    print('\\end{tabular}')


if __name__ == '__main__':
    # Warning: The next test will take a really long time to run.
    # print(solution_a(sys.maxsize-2))

    start_time = time()
    for n in range (1000000, 1000031):
        print(solution_a(n))
    end_time = time()
    print(f"a)运行时间：{(end_time - start_time):.6f}秒")
    for n in range (1000000, 1000031):
        print(solution_b(n))
    print(f"b)运行时间：{(time() - end_time):.6f}秒")

    # print a table with latex
    res = []
    for n in range (1000000, 1000031):
        res.append(solution_b(n))
    print_beauty(res)
