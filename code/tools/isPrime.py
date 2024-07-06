def isPrime(a, b):
    if (b == 0):
        return False
    if (b == 1):
        return True
    return isPrime(b, a%b)

if __name__ == '__main__':
    print(isPrime(165, 13))