
count=0
for i in range(1,78120//2+1):
    if 78120%i==0:
        count+=1
print(count+1)