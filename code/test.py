from tools import RabinMillerTest, isCarmichael, successive_square, sigma, gcd, phi, factoringPrimeFactors

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

# for n in [10, 20, 1728]:
#     print(sigma(n))

# print(successive_square(2, 1000, 2379))
# print(successive_square(567, 1234, 4321))
# print(successive_square(47, 258008, 1315171))
# print(successive_square(7, 7386, 7387))
# print(successive_square(7, 7392, 7393))
# print(factoringPrimeFactors(7387))
# print(factoringPrimeFactors(118901521))
# print(successive_square(2, 9990, 9991))
# print(factoringPrimeFactors(9991))

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

for p in [5, 7, 11, 13, 19]:
    res = set()
    for i in range(1, p):
        res.add(i**3 % p)
    print(f'{p} & {res} \\\\')