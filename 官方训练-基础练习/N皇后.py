#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

class Solution(object):
    def solveNQueens(self, n):
        # 生成N*N的棋盘，填充棋盘，每个格子默认是“。”表示没有放置皇后
        l = [["." for _ in range(n)] for _ in range(n)]
        res = []
        # 判断当前行有效性
        def isVaild(row, col):
            # 判断现在列 有无没有q
            for i in range(row):
                if l[i][col]== "Q":
                    return False
            #判断左上角斜线
            i,j = row - 1, col - 1
            while i>=0 and j>=0:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j-1
            # 判断右上角斜线
            i,j = row - 1, col + 1
            while i>=0 and j<n:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j+1
            return True
        def nQueen(row):
            if row==n:
                res.append( ["".join(l[i]) for i in range(n)] )
                return
            #遍历每一列，也可以每一行
            for col in range(n):
                if isVaild(row, col):
                    #如果这一行有效直接放一个queen
                    l[row][col] = "Q"
                    #然后在下一个地方继续放
                    nQueen(row + 1)
                    # 当row =3 时来到下面这
                    #从后面往前面加.
                    #这代表着还原
                    l[row][col] = "."


        nQueen(0)
        return res


