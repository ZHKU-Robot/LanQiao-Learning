n = 30 #int(input('输入 n'))
a, b, c =2,3,6 # [int(ever) for ever in input('输入a,b,c').split(' ')]
# print(a, b, c)
sum=0
for i in range(n):
    if i%a!=0 and i%b!=0 and i%c!=0:
        print(i)
        sum+=1
print("总数=",sum)

