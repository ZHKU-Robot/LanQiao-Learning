n,m,t=map(int,input().split())
tsList=[]
idList=[]
for i in range(m):
    ts,id_=map(int,input().split())
    tsList.append(ts)
    idList.append(id_)

prior=[0 for i in range(n)]
buf={k:False for k in range(n)}
for second in range(1,t+1):
    if second in tsList:
        #除了这个开始提升，其他所有开始降低
        toImporveIndex=[t for t in range(len(tsList)) if tsList[t]==second]
        toImporveStore=[idList[toi] for toi in toImporveIndex]
        toDecsendStore=set([s for s in idList if s not in toImporveStore])
        for i in toImporveStore:
            prior[i-1]+=2
            if prior[i-1]>5:
                buf[i-1]=True
        for i in toDecsendStore:
            prior[i-1]-=1 if prior[i-1]>0 else 0
            if prior[i-1]<=3:
                buf[i-1]=False
    else:
        #两家的外卖开始减1
        for i in range(len(prior)):
            prior[i]-=1 if prior[i]>0 else 0
            if prior[i]<=3:
                buf[i]=False
    print("第{}秒".format(second))
    print(prior)
    print(buf)

        
    
