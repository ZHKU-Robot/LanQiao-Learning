x = 0
cnt = 0
n = 2020

def check(x):
    if int(pow(x, 0.5)) * int(pow(x, 0.5)) != x:
        return 0
    return 1
        
a = [0, 1, 4, 9]
res = []


def dfs(u, num, flag):
    
    if num == 0:
        if check(u) == 1:
            res.append(u)
            if len(res) >= 1000:
                print(res)
        return 
    for i in range(0, len(a)):
        if flag != 1 and num == flag and i == 0:
                continue
        dfs(int(str(u) + str(a[i])), num-1, flag)
    
num = 1
while True:
    dfs(0, num, num)
    num += 1
    if len(res) >= n:
        break
print(res[2020])
