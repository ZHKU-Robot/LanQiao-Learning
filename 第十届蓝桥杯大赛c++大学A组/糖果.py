
n,m,k=map(int,input().split())

ntk=[list(map(int,input().split())) for i in range(n)]

weight=[0 for i in range(m+1)]
ans=set()
# 考虑到 必须 遍历 一次 来确定 每一次选择的最优解
# 需要用一个 数组来标记 每一袋的 权重
# 注意的是 相同的元素 不能计算,所以用一个set保存一下
count=0
for i in range(m):
    for bag in range(len(ntk)):
        bagSet=set(ntk[bag])
        t=len(bagSet)
        # 如果有相同的要减
        for ever in ans:
            if ever in bagSet:
                t-=1
        weight[bag]=t

    print(weight)
    #选择最多的那个开始
    maxIdx=weight.index(max(weight))
    #将他加入ans
    ans=ans|set(ntk[maxIdx])
    count+=1
    ntk.pop(maxIdx)
    weight.pop(maxIdx)
    if len(ans)==m:
        break
    #
print(count if len(ans)==m else -1)


