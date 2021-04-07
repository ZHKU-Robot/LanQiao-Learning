#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


# n=int(input())

# n-1个空格

inp= [[7],
      [3 ,8],
      [8, 1 ,0],
      [2, 7, 4, 4],
      [4 ,5, 2 ,6, 5]]
n=len(inp)
# 初始化
dp=[[0 for j in range(i)] for i in range(1,n+1)]
dp2=[[(0,0) for j in range(i)] for i in range(1,n+1)]
dp[0][0]=7


def dpPrint():
    for i in dp:
        print((n-len(i)) * ' ', end='')
        print(*i)
def dp2Print():
    for i in dp2:
        print((n-len(i)) * '  ', end='')
        print(*i)
# 先计算初始状态
# 由于只能走两步
for i in range(1,3):
    dp[i][0]=inp[i][0]+dp[i-1][0]
    dp[i][-1]=inp[i][-1]+dp[i-1][-1]
for i in range(1,n):
    dp2[i][0]= (1 + dp2[i-1][0][0],0)
    dp2[i][-1]= ( 0, dp2[i-1][-1][1]+1)

for row in range(2,n):
    for col in range(1,len(inp[row])-1):
        dp2[row][col] = (max([dp2[row - 1][col - 1][0], dp2[row - 1][col][0]]), max([dp2[row - 1][col][1], dp2[row - 1][col - 1][1]]))

# dpPrint()
# 从第3行开始第1个到倒数第二个开始

for row in range(2,n):
    for col in range(1,len(inp[row])-1):
        lh=inp[row][col]+dp[row-1][col-1]
        rh=inp[row][col]+dp[row-1][col]
        left=dp2[row][col][0]
        right=dp2[row][col][1]
        if abs(left-right)<=1: #
            # 只能走右边
            dp[row][col] = rh if rh>lh else lh
        # 取两个的最大值

dp2Print()
dpPrint()

