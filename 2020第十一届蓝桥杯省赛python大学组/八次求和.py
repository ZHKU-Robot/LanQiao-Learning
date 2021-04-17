MOD=123456789
res=0
n=int(input())
for i in range(1,n+1):
    res=(res+pow(i,8,MOD))%MOD
print(res)    
