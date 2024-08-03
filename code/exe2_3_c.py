from tools.prime import gcd

def getPrimitivePythagoreanTriple(target_length = 10):
    t = 1
    s = 3
    result = []
    while result.__len__() < target_length:
        if (gcd(s, t) == 1):
            result.append([s*t, (s*s - t*t)//2, (s*s + t*t)//2, s, t])
        t += 2
        if (s == t):
            t = 1
            s += 2
    return result

if __name__ == '__main__':
    result = getPrimitivePythagoreanTriple(20)
    res = ''
    for i in range(result.__len__()):
        print(result[i])
        res += str(result[i][2]) + ', '
    print(res)