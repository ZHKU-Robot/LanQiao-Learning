#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

m, n=map(int, input().split())
l=[]
for r in range(m):
    l.append([int(i) for i in input().split()])

# 一开始 的方向是向下
down,up,right,left=1,2,3,4

_row=0
_col=0
for r in range(n//2+1):
    print("round",r)
    for c in range(_row,m-_row):
        if l[c][r]!=-1:
            print(l[c][r],end=' ')

            l[c][r]=-1
        _row += 1
    _row-=1
    _col+=1

    for c in range(_col,n-_col+1):
        if l[_row][_col]!=-1:
            print(l[_row][_col],end=' ')
            l[_row][_col]=-1
        _col += 1
    _col-=1
    _row-=1

    for c in range(_row,r-1,-1):
        if l[c][_col]!=-1:
            print(l[c][_col],end=' ')
            l[c][_col]=-1
        _row -= 1
    _row+=1
    _col-=1

    for c in range(_col,r,-1):
        if l[_row][c]!=-1:
            print(l[_row][c],end=' ')
            l[_row][c]=-1
        _col-=1
    _col+=1
    _row+=1
    print()

 # 3 2
 # 1 2
 # 3 4
 # 5 6