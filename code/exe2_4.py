from tools.prime import isPrime

def findPrimitivePythagoreanTripleWithSimpleC(target = 3, num = 1):
    t = 1
    s = 3
    dic = {}
    res = []
    while True:
        if (isPrime(s, t)):
            ppt = [s*t, (s*s - t*t)//2, (s*s + t*t)//2, s, t]
            c = ppt[2]
            record = dic.get(c)
            if record == None:
                dic[c] = [ppt]
            else:
                dic[c].append(ppt)
                if len(dic[c]) == target:
                    res.append(dic[c])
                    num -= 1
                    if (num < 1):
                        return res
        t += 2
        if (t == s):
            t = 1
            s += 2

def format(res):
    return f'{res[0]}^2 + {res[1]}^2'

if __name__ == '__main__':
    result = findPrimitivePythagoreanTripleWithSimpleC(2, 2)[1]
    print(f'{result[0][2]}^2 = {format(result[0])} = {format(result[1])}')
    result = findPrimitivePythagoreanTripleWithSimpleC(3)[0]
    print(f'{result[0][2]}^2 = {format(result[0])} = {format(result[1])} = {format(result[2])}')
    result = findPrimitivePythagoreanTripleWithSimpleC(4)[0]
    print(f'{result[0][2]}^2 = {format(result[0])} = {format(result[1])} = {format(result[2])} = {format(result[3])}')
