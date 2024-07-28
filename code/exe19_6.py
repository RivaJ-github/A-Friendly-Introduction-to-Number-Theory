from tools import isCarmichael

# 100 000以内的卡米歇尔数
# res = []

# for n in range(3, 100000, 2):
#     if (isCarmichael(n)):
#         print(n)
#         res.append(n)

# print(res)


# 大于1000000的最小卡米歇尔数是
n = 1000001
while True:
    if (isCarmichael(n)):
        print(n)
        break
    n += 2
