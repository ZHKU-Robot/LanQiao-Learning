n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
print(arr)
sub=arr[1]-arr[0]
i=1
while i<len(arr)-1:
    if arr[i+1]-arr[i]<sub:
        sub=arr[i+1]-arr[i]
    print(sub)
    i+=1
print((max(arr)-min(arr))//sub+1)
        
        
