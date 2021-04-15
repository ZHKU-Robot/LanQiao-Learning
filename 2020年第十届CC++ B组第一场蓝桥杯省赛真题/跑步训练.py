n=10000

cps=600//60 #  每秒钟消耗的体力
bps=300//60 #每秒钟回复的体力

s=0

run=True
while run:
    count=0
    while count<60:
        n-=cps
        s+=1
        if n==0:
            run=False
            break
        count+=1
    if run:
        n+=300
        s+=60
print(s)