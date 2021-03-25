#一个循环队列而已


n,k=map(int,input().split())

#很简单 nimabi

l=[i for i in range(1,n+1)]

cur=0
while len(l)!=1:
    cur+=k-1
    if cur>=len(l) and len(l)>=k:
        cur=cur%(len(l))
    elif  len(l)<k:
        cur=k%len(l)

    print(l,l[cur],cur)
    l.pop(cur)
print(l)
 
    
