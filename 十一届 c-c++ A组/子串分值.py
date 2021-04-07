

s='ababc'
n=len(s)
count=0
def countOnlyOne(s):
    d={}
    global count
    for _ in s:
        if _ not in d:
            d[_]=1
        else:
            d[_]+=1
#     统计1出现的个数
    count+=list(d.values()).count(1)
for i in range(n):
    for j in range(i+1,n+1):
        countOnlyOne(s[i:j])
print(count)