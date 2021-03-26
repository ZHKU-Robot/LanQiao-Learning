s='''SLANQIAO
ZOEXCCGB
MOAYWKHI
BCCIPLJQ
SLANQIAO
RSFWFNYA
XIFZVWAL
COAIQNAL'''

obj="LANQIAO"

strlines=[]
count=0
#left 2 right &&  right2left
for line in s.split('\n'):
    left2right=len(line.split(obj))-1
    right2left=len(line.split(obj[::-1]))-1 #翻转一下
    strlines.append(line)
    count+=left2right
    count+=right2left

#  翻转 字符串
print(strlines)

transverseStr=[''.join(line) for line in list(zip(*strlines))]
print(transverseStr)
for line in transverseStr:
    left2right=len(line.split(obj))-1
    right2left=len(line.split(obj[::-1]))-1 #翻转一下
    count+=left2right
    count+=right2left


# 判断斜线
i=len(strlines)-1
for col in range(len(strlines-1)):
    j=col
    while i<len(strlines) and j<0:
        print(strlines[i][j])
        i,j=
    
print(count)

