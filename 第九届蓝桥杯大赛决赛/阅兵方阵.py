# 先确定 人数平方的阈值
import math
num=1000
count=0
while count!=12:
    count=0
    limit=int(math.sqrt(num))
    t=0
    for i in range(limit,limit//2,-1):
        iSquare=i**2
        # if 余数 的开方刚好是整的，那么就是可以的
        rest=num-iSquare
        if int(math.sqrt(rest))**2==rest and t!=rest:
##            print(iSquare,rest)
            t=iSquare
            count+=1
    num+=1
print("count",count)
print("num",num)
