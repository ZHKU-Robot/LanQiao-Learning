mrows,ncols=map(int,input().split())
pic=[]
for i in range(mrows):
    pic.append(list(map(int,input().split())))
for rot in list(zip(*pic)):
    print(*rot[::-1])
    
