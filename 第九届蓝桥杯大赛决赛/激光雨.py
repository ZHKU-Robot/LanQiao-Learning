n=int(input())

count=n+1
for i in range(n):
    for j in range(i+2,n):
        count+=1
print(count)
