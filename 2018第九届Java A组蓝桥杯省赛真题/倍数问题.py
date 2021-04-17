n,k=10,3
nl=[i for i in range(1,n+1)]

#从n 里拿出3个数 并且保证 和最大 贪婪的 选取即可
# 首先对输入的数组进行排序
# nl.sort(reverse=True)
# 然后拿到 最大的3个数进行组合
#
#
ans=[]
def dfs(nlIdx,path,flag):

    if flag:
        return True
    if len(path)==3:
        #第一个符合条件的和最大即可
        # print(path)
        s=sum(path)
        if s%k==0:
            # print(path)
            ans.append(path[:])
            return True
    for i in range(nlIdx-1,-1,-1):
        flag=dfs(i,path+[nl[i]],flag)
        if flag:
            return True
    return False
dfs(n,[],False)
print(sum(ans[0]))
