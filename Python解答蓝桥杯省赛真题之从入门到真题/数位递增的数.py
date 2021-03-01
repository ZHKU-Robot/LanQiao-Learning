n=int(input())
c=0
for i in range(1,n+1):
    s=str(i)
    t=s[0]
    f=True
    for j in s[1:]:
        if j>=t:
            t=j
            f=True
            continue
        else:
            f=False
            break
    if f:
##        print(s)
        c+=1
    
print(c)
