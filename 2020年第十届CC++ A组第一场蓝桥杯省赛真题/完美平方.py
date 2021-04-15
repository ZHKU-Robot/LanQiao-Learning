
#
# # 如果一个数没有 0 1 4 9  那么肯定不是完美平方数
import math

n=0
count=0
pref=['0','1','4','9']
while count<2020:
    flag=True
    for num in list(str(n)):
        if  num not in pref:
            flag=False
            break
    if flag:
        half=int(math.sqrt(n))
        if int(half*half)==n:
            print(count)
            count+=1
    n+=1
#
#
# def isWQ(i):
#     flag = True
#     ll = set(list(map(int, list(str(i)))))  # 把这个数的每一位加进集合
#
#     if 2 in ll or 3 in ll or 5 in ll or 6 in ll or 7 in ll or 8 in ll:  # 只要其中有一个不是完全平方数，也就是是2 3 ...当中的一个
#         flag = False  # 则i不是完美平方数
#
#     return flag
#
#
# count = 0
# for i in range(100):  # 从0到1000000开始数
#     if isWQ(i):  # 如果这个数符合要求，count+1
#         print(i)
#         count += 1
#     if count == 2020:  # 如果刚好加到2020，那么输出这个数
#         print(i)
#         break