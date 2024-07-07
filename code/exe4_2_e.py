from tools.prime import factoringPrimeFactors
from exe4_2_a import getSolution

def hasNo4SquareFactors(n):
    primeFactors = factoringPrimeFactors(solution[2])
    for fact in primeFactors:
        if fact[1] // 2 > 1:
            return False
    return True

if __name__ == '__main__':
    for y in range(22, 29):
        solution = getSolution(1, y)
        
        # solution[2]是1+y^3的平方，确保它没有4次方的素因子就能确定它1+y^3没有平方因子
        if (hasNo4SquareFactors(solution[2])):
            print(f'{y} : {solution}')