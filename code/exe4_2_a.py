def getSolution(x, y):
    z = x**3 + y**3
    return (x*z, y*z, z**2)

if __name__ == '__main__':
    for x in range (1, 4):
        for y in range (x, 5):
            print(getSolution(x, y))
