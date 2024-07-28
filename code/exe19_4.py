from tools import factoringPrimeFactors

def isPrime(n): 
    factors = factoringPrimeFactors(n)
    return len(factors) == 1 and factors[0][1] == 1

i = 0
k = 1
while i < 5:
    if (isPrime(6*k+1) and isPrime(12*k+1) and isPrime(18*k+1)):
        print(k)
        print((6*k+1)*(12*k+1)*(18*k+1))
        i += 1
    k += 1
