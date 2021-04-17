n,m=map(int , input().split())
alist=list(map(int,input().split()))

## 找到n+1个最大的数 和n个最小的数
_sum=0
for i in range(n+1):
    _max=max(alist)
    alist.pop(alist.index(_max))
    _sum+=_max

for j in range(m):
    _min=min(alist)
    alist.pop(alist.index(_min))
    _sum-=_min
print(_sum)

