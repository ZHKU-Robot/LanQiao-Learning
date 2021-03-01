MOD = 2020
N = 10
dp = [[0 for j in range(N)] for i in range(N)]
n = 10

dp[0][0] = 1 # 不放也是方案
        
for i in range(0, n+1):
    for j in range(0, n+1):
        if i != 0 and i >= j-1: # 转移前的状态也要合法，即第一行的数量不小于第二行的数量
            dp[i][j] = (dp[i][j] + dp[i-1][j])%MOD
        if j != 0 :
            dp[i][j] = (dp[i][j] + dp[i][j-1])%MOD
        print(dp)
print(dp[n][n]) 
