import math
from tools import gcdWithXY, indexI, primitive_root_m, epa, primitive_root, LiouvilleLambda, isPrime, DesentProcedure_1, DesentProcedure_2, DesentProcedure, JacobiSymbol, RabinMillerTest, isCarmichael, successive_square, sigma, gcd, phi, factoringPrimeFactors

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

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
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

# for n in [30, 504, 60750]:
#     print(LiouvilleLambda(n))

# for (m, a) in [(9, 2), (15, 2), (16, 3), (10, 3)]:
#     for i in range(1, m):
#         if successive_square(a, i, m) == 1:
#             print(i)
#             break

# for m in range(11, 21, 2):
#     for i in range(1, m):
#         if successive_square(2, i, m) == 1:
#             print(f'e_{m}={i}')
#             break

# proots = primitive_root(13)
# print(proots)
# for r in range(2, 9):
#     print([successive_square(p, r, 13) for p in proots])
# res = []
# for p in primeList:
#     if 3 in primitive_root(p):
#         res.append(p)
# print(res)

# for m in range(2, 51):
#     if (len(primitive_root_m(m)) == 0):
#         print(m)

# print(primitive_root_m(17))

# print(' & '.join([str(successive_square(3, i, 17)) for i in range(1, 17)]))

# for i in range(1, 17):
#     j = successive_square(3, i, 17)
#     print(' & '.join([str(1 if k == j else 0) for k in range(1, 17)]), end="\\\\\n")

# print(' & '.join([str(a) for a in range(1, 47)]))
# print(' & '.join([str(I) for I in indexI(47, 5)]))
# print(indexI(37, 2))


# p = 380803
# g = 2
# k = 278374

# r = 198374
# a = successive_square(g, k, p)
# e1 = successive_square(g, r, p)
# e2 = successive_square(a, r, p) * 302526 % p
# print(e1, e2)


# for (e1, e2) in [(61745, 206881), (255836, 314674),(108147, 350768)]:
#     c = successive_square(e1,k, p)
#     (_, u, _) = gcdWithXY(c, p)
#     v = u * e2 % p
#     print(v)

x0, y0 = 9, 4
for i in range(1, 6):
    x0, y0 = 9*x0+20*y0, 4*x0 + 9*y0
    print(f'({x0}, {y0}),', end='')