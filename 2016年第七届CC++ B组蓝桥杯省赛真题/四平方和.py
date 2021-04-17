import math
from functools import reduce
#


l=[0,0,0,0]
def fastPower(base):
    res=1
    exp=2
    while exp:
        if exp&1==1:
            res*=base
        exp=exp>>1
        base*=base

    return res
#
#
def powerSum(l):
    # print(l)
    return sum(map(fastPower,l))
#
# ans=[]
# def dfs(num,idx):
#
#
#     if idx<0:
#         return
#     for i in range(1,num+1):
#         # print(l)
#         l[idx] = i
#         # 判断当前平方和
#         ps=powerSum(l)
#         if ps>n:
#             # tnum-=1
#             continue
#         elif ps==n:
#             # print(l)
#             cop=l.copy()
#             if cop not in ans:
#                 ans.append(cop)
#
#         # else:
#         #     pass
#         # print(l)
#         dfs(i,idx-1)
#         l[idx]=0
#         # if ans:
#         #     return
#         # num+=1
#         # l[idx]=0
# dfs(maxNum,3)
# print

# 一直取 max num
#
# a, b, c, n;
# 	double Max, d;
# 	scanf("%d", &n);
# 	Max = sqrt(n);
# 	for(a = 0; a <= Max; a ++){
# 		for(b = a; b <= Max; b ++){
# 			for(c = b; c <= Max; c ++){
# 				d = sqrt(n - a*a - b*b - c*c);
# 				if(d == (int)d){//看d是不是整数
# 					printf("%d %d %d %d\n", a, b, c, (int)d);
#                     return 0;
# 				}
# 			}
# 		}
# 	}
#
n=773535
def get():
    max=int(math.sqrt(n));
    for a in range(max):
        for b in range(a,max):
            for c in range(b,max):
                res=n-a*a-b*b-c*c
                if res>=0:
                    d=math.sqrt(res)
                    if d==int(d):
                        print(a,b,c,int(d))
                        return 0
get()