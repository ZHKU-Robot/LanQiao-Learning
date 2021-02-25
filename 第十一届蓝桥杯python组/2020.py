#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


s="""0020002200
2220200202
2222000202
0202202002
0022202000
0002022222
0202022002
0220022020
0022222200
0020202002
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
for k2 in range(col):
    i, j = row-1 , k2
    t=''
    while i>=0 and j>=0:

        t+=sl[i][j]
        i,j = i-1,j-1
    # 左上斜线
    obliqueCount+=t.count('2020')

    t=''
    i,j = row - 1, k2
    while i>=0 and j<col:
        t+=sl[i][j]
        i,j = i-1,j+1
#     右上斜线
    obliqueCount += t.count('2020')
print(obliqueCount)