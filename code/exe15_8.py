def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

res = []
p = 2 # e=1
for e in range(2, 101):
    p += 1
    p *= 2
    p -= 1
    if not is_prime(p): 
        continue
    q = 2 * p + 1
    if not is_prime(q):
        continue
    r = (p + 1) * (q + 1) - 1
    if not is_prime(r):
        continue
    k = (p + 1) * 2 // 3
    print((e, p, q, r, k*p*q, k*r))