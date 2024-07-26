from tools import sigma, gcd, phi, factoringPrimeFactors

# for i in range(11, 21):
#     print(i ** 1000 % 10000)

# print(phi(10000))

# for i in range(1000000):
#     if len(factoringPrimeFactors(i)) == 1 and i ** 1000 % 10000 != 1:
#         print(i)
#         break

# print(443**4 % 10000)

# print(factoringPrimeFactors(257))

# i = 4
# while True:
#     factors = factoringPrimeFactors((3**i - 1) // 2)
#     if (len(factors) == 1 and factors[0][1] == 1):
#         print(i)
#         break
#     i += 1

# print(gcd(213408, 2205))

for n in [10, 20, 1728]:
    print(sigma(n))