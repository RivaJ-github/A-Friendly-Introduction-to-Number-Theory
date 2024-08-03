from tools import LiouvilleLambda, isPrime, DesentProcedure_1, DesentProcedure_2, DesentProcedure, JacobiSymbol, RabinMillerTest, isCarmichael, successive_square, sigma, gcd, phi, factoringPrimeFactors

# for i in range(11, 21):
#     print(i ** 1000 % 10000)

# print(phi(10000))

# for i in range(1000000):
#     if len(factoringPrimeFactors(i)) == 1 and i ** 1000 % 10000 != 1:
#         print(i)
#         break

# print(factoringPrimeFactors(5929))
# for m in [4370, 1885, 1189, 3185]:
#     print(factoringPrimeFactors(m))

# i = 4
# while True:
#     factors = factoringPrimeFactors((3**i - 1) // 2)
#     if (len(factors) == 1 and factors[0][1] == 1):
#         print(i)
#         break
#     i += 1

# print(gcd(264, 275))

# for n in [10, 20, 1728]:
#     print(sigma(n))

# print(successive_square(2, (1293337 - 1) // 2, 1293337))
# print(JacobiSymbol(11, 1729))
# print(factoringPrimeFactors(12049))

# for i in [1105, 1235, 2821, 6601, 8911, 10659, 19747, 105545, 126217, 162401, 172081, 188461]:
#     print(i)
#     print(factoringPrimeFactors(i))
#     print(isCarmichael(i))

# print(isCarmichael(3))

# print([
#     RabinMillerTest(i) for i in [155196355420821961, 155196355420821889, 285707540662569884530199015485750433489, 285707540662569884530199015485751094149]
# ])

# res = []
# for i in range(1, 10):
#     r = i ** 2 % 19
#     res.append(r)
# print(res)

# for p in [3, 5, 7, 11, 13, 17, 19]:
#     A = 0
#     for i in range(1, (p+1)//2):
#         A += (i**2) % p
#     B = (p - 1) // 2 * p - A
#     print(f'{p} & {A} & {B} \\\\')

# for p in [5, 7, 11, 13, 19]:
#     res = set()
#     for i in range(1, p):
#         res.add(i**3 % p)
#     print(f'{p} & {res} \\\\')

# A = [11, 13, 23, 37, 47, 59, 61, 71, 73, 83, 97, 107, 109]
# B = [5, 7, 17, 19, 29, 31, 41, 43, 53, 67, 79, 89, 101, 103, 113, 127]
# m = 12
# a = [n % m for n in A]
# b = [n % m for n in B]
# print(a)
# print(b)

# print(JacobiSymbol(37603, 48661))
# print(JacobiSymbol(85, 101))
# print(JacobiSymbol(29, 541))
# print(JacobiSymbol(101, 1987))
# print(JacobiSymbol(31706, 43789))
# print(JacobiSymbol(299, 397))
# print(JacobiSymbol(14, 137))
# print(JacobiSymbol(55, 179))

# primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# # for p in range(5, 101, 2):
# #     factors = factoringPrimeFactors(p)
# #     if len(factors) == 1 and factors[0][1] == 1:
# #         primeList.append(p)
# # print(primeList)

# for p in primeList:
#     print(f'&{p}', end='')
#     a = 1
#     flag = False
#     while (a ** 2 < p):
#         b = 0
#         while b <= a and b ** 2 + a ** 2 <= p:
#             c = 0
#             while c <= b and c ** 2 + b ** 2 + a ** 2 <= p:
#                 if c ** 2 + b ** 2 + a ** 2 == p:
#                     print(f'={a}^2+{b}^2+{c}^2', end='')
#                     flag = True
#                 c += 1
#             b += 1
#         a += 1
#     if not flag:
#         print('=None', end='')
#     print('\\\\')

# print(DesentProcedure(261, 947, 10, 96493))

# for n in range(1, 301):
#     f = (n**2) - n + 41
#     if (not isPrime(f)):
#         # print(f'{n}, {f} is prime')
#         print(f'{n}, {f} is not prime')
#         break

for n in [30, 504, 60750]:
    print(LiouvilleLambda(n))