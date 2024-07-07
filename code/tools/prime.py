def isPrime(a, b):
    if (b == 0):
        return False
    if (b == 1):
        return True
    return isPrime(b, a%b)

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

        

if __name__ == '__main__':
    # print(isPrime(165, 13))
    print(factoringPrimeFactors(12))