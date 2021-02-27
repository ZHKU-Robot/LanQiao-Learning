f=[[ 0 for i in range(1011)]for i in range(1011)]
f[0][0]=1
for i in range(1011):
    for j in range(1011):
        if i>j:
            f[i][j]+=f[i-1][j]
        if j!=0:
            f[i][j]+=f[i][j-1]
        f[i][j]%=2020
print(f[-1][-1])
