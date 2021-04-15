n=5
m=5
ans=0
dire=((1,0),(0,1))
vis=[[0]*m for i in range(n)]
def dfs(row,col):

    global ans
    if row==n-1 and col==m-1:
        ans+=1
        vis[row][col]='@'
        for v in vis:
            print(*v)
        print()
        return False
    if row%2==0 and col%2==0:
        return False
    if vis[row][col]=="#":
        return False

    vis[row][col]='#'

    for d in dire:
        trow,tcol=row+d[0],col+d[1]
        if 0<=trow<n and 0<=tcol<m:
            dfs(trow,tcol)
            vis[trow][tcol]=0

        # print(vis)


vis[n-1][m-1]="@"
dfs(1,1)
print(ans)