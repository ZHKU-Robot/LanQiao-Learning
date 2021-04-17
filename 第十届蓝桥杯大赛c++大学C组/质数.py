i=2
c=0
while 1:
    for j in range(2,i+1):
        if i%j==0 and i!=j:
            j=0
            break
        else:
            j=1
    if j:
##        print(i,"是质数")
        c+=1
    i+=1
    if c==2020:
        print(i)
        break

           
