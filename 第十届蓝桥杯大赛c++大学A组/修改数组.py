n=int(input())
l=list(map(int,input().split()))
temp=l[0]
for idx in range(1,n):
     if temp!=l[idx]:
         temp=l[idx]
         continue
     else:
         # 尝试对ever++ 直到不重复
        while 1:
            l[idx]+=1
            if l.count(l[idx])==1:
                break

print(l)