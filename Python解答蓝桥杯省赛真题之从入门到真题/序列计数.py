n=int(input())
c=n
d={}
def rec(l:list,i:int):
    global c
    print(l)
    three=abs(l[i]-l[i+1])
    if three in d:
        c+=d[three]
        return
    else:
        d[three]=i
    
    for j in range(1,three+1):
        if j<three:
            if abs(l[i+1]-j) not in d:
                c+=1
            rec(l+[j],i+1)
        else:
            break
    
for i in range(1,n):
    l=[n,i]
    t=c
    rec(l,0)
print(c)

