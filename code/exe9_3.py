for m in [4,6,8,9,10,12,14,15,16,18, 20]:
    mult = 1
    for i in range(1, m):
        mult *= i
    print(mult % m)