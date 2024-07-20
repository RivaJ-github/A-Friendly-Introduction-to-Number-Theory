from math import log

def intt(t):
    ln = log(t)
    res = log(ln) + ln
    item = ln
    for i in range(2, 101):
        item *= ln * (i - 1) / i / i
        res += item
    return res

if __name__ == '__main__':
    int2 = intt(2)
    lst = [10, 100, 1000, 10**4, 10**6, 10**9]
    for x in lst:
        print(f'{x/log(x):.2f}')
    for x in lst:
        print(f'{intt(x) - int2:.2f}')