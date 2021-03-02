n,m=map(int,input().split())
grass=[]
for i in range(n):
    grass.append(list(input()))
k=int(input())
mouth=0

def dfs(mouth,i,j):
    print(i,j,mouth)
    if mouth==k or j>=m or i>=n or j<0 or i<0:
        return
    else:
            if j<m-1:
                grass[i][j+1]='g'
                dfs(mouth+1,i,j+1)
            if i<n-1:
                grass[i+1][j]='g'
                dfs(mouth+1,i+1,j)
            if j>0:
                grass[i][j-1]='g'
                dfs(mouth+1,i,j-1)
            if i>0:
                grass[i-1][j]='g'
                dfs(mouth+1,i-1,j)
##            showgrass()
            
            
def showgrass():
    for row in grass:
        print(''.join(row))
 

pos=[]               
for row in range(n):
    for col in range(m):
        if grass[row][col]=='g':
            pos.append((row,col))
for x,y in pos:
    dfs(0,x,y)
        
showgrass()
