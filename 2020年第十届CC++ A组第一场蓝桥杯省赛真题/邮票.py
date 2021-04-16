# 从 每一个位置开始剪 5个 应该是bfs

from collections import deque

n, m = 3, 4

s=set()
def dfs(row,col,leng,paper):
    if leng==5:
        string=''
        for p in paper:
            print(*p)
            string+=''.join(map(str,p))
        print()
        #加入集合防止重复
        s.add(string)


        return
    for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
        trow,tcol=row+dx,col+dy
        if 0<=trow<n and 0<=tcol<m and vis[trow][tcol]!=1:
            vis[trow][tcol]=1
            paper[trow][tcol]=1
            dfs(trow,tcol,leng+1,paper)
            #回溯
            paper[trow][tcol]=0
            vis[trow][tcol]=0
for i in range(n):
    for j in range(m):
        paper = [[0] * m for i in range(n)]
        vis = [[0] * m for i in range(n)]

        vis[i][j] = 1
        paper[i][j] = 1
        dfs(i,j,1,paper)
print(len(s))

