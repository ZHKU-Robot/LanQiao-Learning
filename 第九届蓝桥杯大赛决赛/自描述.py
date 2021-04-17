n=int(input())

if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(2)
else:
    curGn=2
    gnLeng=3
    t=0
    curN=3
    while gnLeng<n:
        if t<curGn:
            t+=1
        else:
            t=0
            gnLeng+=curGn
   
            curGn+=1
    print(curGn)
