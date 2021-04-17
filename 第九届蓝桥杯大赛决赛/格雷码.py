n,k=map(int,input().split())

s=0

count=0

while 1:
    print(n,k)
    k+=k
    if(k>=n):
        k=k%n
    count+=1
    if n%k!=0:
        break
print(count)
