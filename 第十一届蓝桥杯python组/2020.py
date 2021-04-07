#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


s="""220000
000000
002202
000000
000022
002020
"""
def transformMatrix(m):
    # 逆向参数收集，将矩阵中多个列表转换成多个参数，传给 zip
    return list(zip(*m))
sl=[]
rowN=0
colN=0
for i in s.splitlines():
    rowN+=i.count('2020')
    sl.append(list(i))
s2=transformMatrix([list(i) for i in s.splitlines()])

for sen in sl:
    colN+= ''.join(sen).count('2020')

row=len(sl)
col=row

print(s)
obliqueCount=0

def find2020(s):
    count = 0
    while 1:
        flag = s.find('2020')
        if flag == -1:
            break
        s = s[flag + 2:]
        count += 1
    return count

for k2 in range(col):
    i, j = row-k2-1 , 0
    t=''
    while i<row and j<col:
        t+=sl[i][j]
        i,j = i+1,j+1

    # 左上斜线
    obliqueCount+=find2020(t)
    t=''
    i,j = 0, k2+1
    while i<row and j<col:
        t+=sl[i][j]
        i,j = i+1,j+1
#     右上斜线
    obliqueCount += find2020(t)
print(rowN,colN,obliqueCount)
