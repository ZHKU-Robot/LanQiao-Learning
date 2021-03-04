n,m=map(int,input().split())
likes=list(map(int,input().split()))

maxList=[max(likes[:n-m+1])]
maxIndex=likes.index(maxList[0])
i=1
while len(maxList)<m:
    maxList.append(max(likes[maxIndex+1:n-m+i+1]))
    maxIndex=likes.index(maxList[i])
    i+=1
    
print(*maxList)
        

