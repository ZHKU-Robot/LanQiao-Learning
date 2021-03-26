
n=6
while 1:
    t=n
    if t%5==1:
        t-=(t-1)//5
        if t%5==2:
            t-=(t-2)//5
            if t%5==3:
                t-=(t-3)//5
                if t%5==4:
                    t-=(t-4)//5
                    if t%5==0:
                        break
    n+=5
    print(n)
