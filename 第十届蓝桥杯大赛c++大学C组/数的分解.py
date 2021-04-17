def isInvalid(num):
    return True if ('2'  in str(num)) or ('4'  in str(num)) else False
count=0
for i in range(1,2019):
    if  isInvalid(i):
        continue
    for j in range(i+1,2019):
        if i+j>2019:
            continue
        if  isInvalid(j):
            continue
        for k in range(j+1,2019):
            if i + j +k> 2019:
                continue
            if  isInvalid(k):
                continue
            if i+j+k==2019:
                count+=1

print(count)
