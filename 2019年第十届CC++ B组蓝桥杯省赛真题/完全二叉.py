n=int(input())
treeNodes=list(map(int,input().split()))
depth=1
perRowSum=[]
curIndex=0
while 1:
    rowNodes=2**(depth-1)
    if curIndex<len(treeNodes):
        perRowSum.append(sum(treeNodes[curIndex:curIndex+rowNodes]))
    else:
        if curIndex!=len(treeNodes):
            perRowSum.append(sum(treeNodes[curIndex:]))
        break
    curIndex+=rowNodes
    depth+=1
print(perRowSum.index(max(perRowSum))+1)
