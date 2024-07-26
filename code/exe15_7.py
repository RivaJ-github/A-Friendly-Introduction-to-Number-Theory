from tools import sigma

res = [0, 0, 0]
for n in range(2, 101):
    s = sigma(n)
    if s < 2 * n:
        res[0] += 1
    elif (s == 2 * n):
        res[1] += 1
    else:
        res[2] += 1
print(res)

res = [0, 0, 0]
for n in range(101, 201):
    s = sigma(n)
    if s < 2 * n:
        res[0] += 1
    elif (s == 2 * n):
        res[1] += 1
    else:
        res[2] += 1
print(res)