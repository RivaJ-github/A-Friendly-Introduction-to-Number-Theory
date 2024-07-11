from tools.prime import gcdWithXY

def hasSolution(n):
    x = y = z = 0
    while True:
        sum = 6*x + 10*y + 15*z
        if sum == n:
            return True
        elif sum > n:
            if y == 0 and z == 0:
                return False
            if z == 0:
                y = 0
                x += 1
            else:
                z = 0
                y += 1
        else:
            z += 1
        
    return False

if __name__ == '__main__':
    res = []
    for i in range(1, 1000):
        if (not hasSolution(i)):
            res.append(i)
    print(res)
