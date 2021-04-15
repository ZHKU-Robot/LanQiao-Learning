
# 看起来是个递归
n,m=3,4
grids=[[-1]*m for i in range(n)]
def isVaild(row,col):
    # print(row,col)
    if col-1>=0: #判断左
        # print("判断左边")
        if grids[row][col-1]!=-1:
            return False
        #判断左上
        if row-1>=0:
            if grids[row-1][col-1]!=-1:
                return False
        #判断左下
        if row+1<n:
            if grids[row+1][col-1]!=-1:
                return False
    if col+1<m:#判断右边
        # print("判断右边")
        if grids[row][col+1]!=-1:
            return False
        if row-1>=0:# 判断右上
            if grids[row-1][col+1]!=-1:
                return False
        if row+1<n:
            if grids[row+1][col+1]!=-1:
                return False
    #判断上面
    if row-1>=0:
        # print("判断上面")
        if grids[row-1][col]!=-1:
            return False
    if row+1<n:
        # print("判断下面")
        if grids[row+1][col]!=-1:
            return False
    return True
s=set()
def count(row, col):

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            if i==n-1 and j == m-1:
                break
            if isVaild(i,j):
                s.add((i,j))
                grids[i][j]='#'
    for grid in grids:
        print(*grid)
    print()
for i in range(n):
    for j in range(m):
        if i ==0 and j==0:
            continue
        if i==n-1 and j==m-1:
            break
        grids[i][j]='#'
        count(i,j)
        grids = [[-1] * m for i in range(n)]

"""

-1 # -1 #
-1 -1 -1 -1 9*8*7*6
# -1 # -1

-1 -1 # -1 9*8*7
# -1 -1 -1
-1 -1 # -1

-1 -1 -1 #
-1 # -1 -1 9*8
-1 -1 -1 -1

-1 -1 -1 -1
# -1 # -1 9*8
-1 -1 -1 -1

-1 # -1 -1
-1 -1 -1 # 9*8*7
# -1 -1 -1


-1 # -1 #
-1 -1 -1 -1 9*8*7
-1 # -1 -1



Process finished with exit code 0

"""
# 上面的加一下就是答案